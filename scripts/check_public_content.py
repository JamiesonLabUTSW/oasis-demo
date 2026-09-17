#!/usr/bin/env python3
"""Validate the public file allowlist and reviewed demo hashes (no network)."""
import hashlib
import json
from pathlib import Path, PurePosixPath
import re
import subprocess
import sys
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
CATEGORIES = {"documentation", "governance", "site", "runtime-manifest",
              "original-synthetic", "public-domain-reference"}
CONTENT = {"original-synthetic", "public-domain-reference"}


def validate(root, inventory, proposed):
    errors = []
    if inventory.get("schema_version") != 1:
        errors.append("Unsupported inventory schema")
    entries = inventory.get("files", {})
    sources = inventory.get("provenance", {})
    if not isinstance(entries, dict) or not isinstance(sources, dict):
        return ["Inventory files and provenance must be objects"]
    for name in sorted(proposed - set(entries)):
        errors.append(f"Unlisted file: {name}")
    for name in sorted(set(entries) - proposed):
        errors.append(f"Inventory entry has no proposed file: {name}")

    for key, source in sources.items():
        if not isinstance(source, dict):
            errors.append(f"Invalid provenance: {key}")
            continue
        kind = source.get("kind")
        fields = ["kind", "creator", "reviewed_on", "rights", "statement"]
        if kind == "public-domain-reference":
            fields += ["source_url", "rights_evidence_url", "jurisdiction", "attribution"]
        elif kind == "original-synthetic":
            fields += ["created_on"]
        else:
            errors.append(f"Unapproved provenance kind: {key}")
        if any(not isinstance(source.get(f), str) or not source[f].strip() for f in fields):
            errors.append(f"Incomplete provenance: {key}")
        if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", source.get("reviewed_on", "")):
            errors.append(f"Invalid review date: {key}")
        if kind == "public-domain-reference":
            for field in ("source_url", "rights_evidence_url"):
                url = urlparse(source.get(field, ""))
                if url.scheme != "https" or not url.netloc:
                    errors.append(f"Invalid public evidence URL: {key}/{field}")

    for name, entry in entries.items():
        if not isinstance(entry, dict):
            errors.append(f"Invalid file entry: {name}")
            continue
        path = PurePosixPath(name)
        if path.is_absolute() or ".." in path.parts or str(path) != name:
            errors.append(f"Unsafe path: {name}")
            continue
        actual = root / name
        if (not actual.resolve().is_relative_to(root.resolve())
                or actual.is_symlink() or not actual.is_file()):
            errors.append(f"Not a regular file: {name}")
            continue
        kind = entry.get("kind")
        if kind not in CATEGORIES:
            errors.append(f"Unapproved file category: {name}")
        if name.startswith("demos/") and kind not in CONTENT:
            errors.append(f"Demo file lacks admitted content category: {name}")
        if kind in CONTENT:
            source = sources.get(entry.get("provenance"), {})
            if source.get("kind") != kind:
                errors.append(f"Missing/mismatched provenance: {name}")
            if not re.fullmatch(r"[0-9a-f]{64}", entry.get("sha256", "")):
                errors.append(f"Demo file lacks reviewed SHA-256: {name}")
        if "sha256" in entry:
            observed = hashlib.sha256(actual.read_bytes()).hexdigest()
            if observed != entry["sha256"]:
                errors.append(f"Reviewed bytes changed: {name}")
    return errors


def main():
    try:
        inventory = json.loads((ROOT / "content-inventory.json").read_text())
        # Includes staged/tracked files AND untracked candidates; ignores .git internals.
        result = subprocess.run(
            ["git", "ls-files", "-z", "--cached", "--others", "--exclude-standard"],
            cwd=ROOT, check=True, capture_output=True,
        )
        proposed = set(result.stdout.decode().rstrip("\0").split("\0"))
        errors = validate(ROOT, inventory, proposed)
    except (OSError, ValueError, subprocess.CalledProcessError) as exc:
        print(f"Public-content check failed: {exc}", file=sys.stderr)
        return 1
    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    print(f"PASS: {len(proposed)} files inventoried; reviewed asset hashes match.")
    print("Content/rights truth and remote images still require human review.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
