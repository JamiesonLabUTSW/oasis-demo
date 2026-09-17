# Contributing

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
4. Update the README catalog and HTML page together. Use precise status:
   browser exercise, assisted installation, or host acceptance pending.
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

## Runtime and support

Runtime/image/platform changes require separate release evidence. Preserve the
existing license/notices and frozen image selection during site edits.
Keep actual site journals in the host's approved private workspace.
Follow the [support guide](docs/support.md) for public reports.
