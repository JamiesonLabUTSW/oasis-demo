# Agent instructions

This is the PUBLIC OASIS demo entry point. Read `docs/audience-guide.md`,
`docs/public-content-policy.md` and `content-inventory.json` before changing
content. Read `docs/runtime.md` for current platform/publication status and
`CONTRIBUTING.md` for the evidence workflow. The supplied installation kit,
application source and private host journal are separate authorities.

- Admit only original synthetic demo content or specifically verified
  public-domain sources. Do not copy private fixtures, institutional rubrics,
  workshop packets, real/de-identified notes, recordings, screenshots, or secrets.
- Synthetic does not automatically mean cleared for public distribution.
  Public-domain media does not clear an accompanying authored rubric.
- Inspect every archive member, workbook sheet, embedded asset, and image layer
  before proposing such artifacts. A clean README is insufficient.
- Register every file in the inventory. Demo assets need provenance and SHA-256.
  Changed bytes require content review, not an automatic hash refresh.
- Preserve `LICENSE`, `THIRD_PARTY_NOTICES`, `images.json`, and
  `images-arm64.json` during ordinary site/documentation edits. Exact selection
  changes require their own reviewed evidence and explicit task scope.
- Distinguish available content, assembled source/notice evidence, anonymous
  release/image downloads, installation, model inference and host acceptance.
  Never infer one from another or claim a run you did not perform.
- Documentation changes do not authorize runtime operations, authentication
  changes, provider/model calls, package publication or protected-data use.
  Preserve saved results; no replay is needed to document an existing receipt.
- Third-party source/test assets retain upstream terms. Inventory small sanitized
  source/license manifests and review receipts as governance/documentation, with
  hashes; this does not admit their contents as public-domain/synthetic demo data.
  Do not edit frozen published archives or erase documented source gaps.
- Keep `index.html` offline-capable and keyboard accessible. No external scripts,
  fonts, embeds, tracking, or credential forms. Never commit a generated login
  helper, private device details, conversations, or deployment journals.
- Run `python3 -B scripts/check_public_content.py` and `git diff --check`.
  Inspect desktop/mobile layouts and interactive controls after visual changes.

Report changed files, actual checks, evidence scope and remaining gates. Use
only sanitized public paths/identities; do not copy raw operator receipts or
journals. Current status belongs in navigation/runtime pages; keep historical
review records clearly dated. See `CONTRIBUTING.md` for the complete workflow.
