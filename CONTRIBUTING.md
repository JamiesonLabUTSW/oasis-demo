# Contributing

Start at the [audience guide](docs/audience-guide.md) to see the visitor's path.
This repository owns the public library, documentation, file inventory and
release-evidence summaries. It does not contain the application source, a
complete installation kit or recipient runtime data. Product fixes and kit
changes follow their own source/release review before public instructions change.

Keep the visitor's path short: choose a demo, understand its inputs, try it,
and find the next installation or review step.

## Add or change a demo

1. Read the [content policy](docs/public-content-policy.md). Establish provenance
   for every note, rubric, recording, transcript, image, and export.
2. Give the demo a folder under `demos/` with purpose, inputs, rights, steps,
   illustrative outputs, and actual test status. Label fictional material.
3. Record each file in [the inventory](content-inventory.json). Demo assets
   need provenance and SHA-256. Never stage private data while deciding whether
   it is publishable.
4. For a catalog or presentation change, update its README and HTML entries
   consistently. Documentation-only work need not change the site or demo bytes.
   Use precise status: manual/browser exercise, saved-result tour, assisted
   installation, or host acceptance pending.
5. Run checks and inspect the full diff. If a runtime execution occurred,
   preserve a sanitized receipt with package/model identifiers, input hashes,
   reviewed output, and limitations.
6. Open a PR describing the user-facing change, provenance, and checks.
   Maintainers review the content itself, not just CI.

## Checks and preview

Python 3.10+; no additional dependencies or model calls:

```bash
python3 -B scripts/check_public_content.py
git diff --check
```

Open `index.html` in a browser. Check wide/narrow layouts, keyboard navigation,
answer reveal controls, downloads, and links. Optional loopback HTTP preview:

```bash
python3 -m http.server 8765 --bind 127.0.0.1
```

Serve only this public repository, never an installation directory or generated
login helper. The site has no build step or backend. GitHub Pages is not enabled
by this change; hosting requires a separate publishing decision.

## Review documentation and readiness claims

Use [runtime details](docs/runtime.md) as the platform/publication reference.
Update claims from the exact supporting receipt, not from a passing documentation
check or another computer's result. Keep these distinct:

- Content/provenance review and its limitations.
- Source/notice evidence assembled and release assets actually downloadable.
- Exact container image publication and anonymous byte verification.
- Recipient installation, sign-in, sample visibility and retained restart.
- Actual model route, bounded task, human review and reopened export.

Write for the audience affected. User instructions need prerequisites, the next
visible action, expected outcome and recovery route. Facilitators need named
inputs, teaching objectives, actual demonstration format and a fallback.
Developers and agents need exact selections, evidence scope and checks. State
what remains untested; avoid copying a host's operational history into the public
guide. Keep dated review records distinct from current navigation/status pages.

## Source, SBOM and license-evidence changes

A software bill of materials (SBOM) lists detected software components. It does
not by itself establish every component's rights or complete source provenance.
The [ARM64 companion](docs/third-party/4abb0bb2-arm64-r1/README.md) and
[review summary](docs/content-review-arm64-2026-09-17.md) show the current bounded
record; their exact artifacts must not be silently replaced.

1. Identify the exact platform, application revision, package bindings and image
   digests. Review every selected image layer and archive payload within a stated
   scope; exclude optional components lacking release clearance.
2. Bind source archives, notices and build references to recorded versions and
   complete hashes. Distinguish acquired sources, reference-only gaps and disabled
   components. Never substitute an adjacent release while claiming an exact match.
3. Inspect every archive member and embedded asset. Upstream test media or
   source-support models remain third-party source fixtures under upstream terms;
   they are not admitted as synthetic/public-domain demo inputs.
4. Keep raw acquisition paths, private metadata and operator receipts outside
   this repository. A sanitized SBOM must preserve component/image identity and
   valid relationships. Record the transformation and verify the public copy.
5. Put large reviewed source/SBOM archives in a separately authorized release.
   Keep only small sanitized manifests, notice guidance and review/publication
   summaries here, inventoried as governance or documentation with hashes. Do not
   bypass the content policy by relabeling demo data as documentation.
6. Obtain independent review of the frozen bytes and limits. Keep assembly status
   separate from availability: only an actual publication and anonymous full-byte
   hash/size check establishes the latter. Published immutable assets require a
   new version for changed bytes, with an updated review and inventory.

A source companion is not a complete application kit. Public access does not
change [project terms](LICENSE) or replace third-party notices. Preserve license,
notice and both platform image-manifest bytes during ordinary documentation work.
Do not claim universal license clearance, a signed/production release, offline
readiness or fresh-machine acceptance from these checks.

## Agent handoff and reporting

Follow [AGENTS.md](AGENTS.md). Before editing, identify the owned files and the
current authoritative status. Work on the requested surface; no runtime,
authentication, model or publication action follows merely from a documentation
task. Use invented or already admitted public examples for offline checks.

In the PR or handoff, list the concrete change, files/content reviewed, checks
actually run, exact artifact identities when relevant, and remaining gates with
an owner or next step. Do not include private paths, credentials, participant
records or raw diagnostics. A local check, a pushed commit, hosted CI and a
published artifact are different events; report each only when verified.

Keep actual site journals in the host's approved private workspace.
Follow the [support guide](docs/support.md) for public reports.
