# Agent instructions

This is the PUBLIC OASIS demo entry point. Read `docs/public-content-policy.md`
and `content-inventory.json` before adding content.

- Admit only original synthetic demo content or specifically verified
  public-domain sources. Do not copy private fixtures, institutional rubrics,
  workshop packets, real/de-identified notes, recordings, screenshots, or secrets.
- Synthetic does not automatically mean cleared for public distribution.
  Public-domain media does not clear an accompanying authored rubric.
- Inspect every archive member, workbook sheet, embedded asset, and image layer
  before proposing such artifacts. A clean README is insufficient.
- Register every file in the inventory. Demo assets need provenance and SHA-256.
  Changed bytes require content review, not an automatic hash refresh.
- Preserve `LICENSE`, `THIRD_PARTY_NOTICES`, and `images.json` in site edits.
- Distinguish available content, image publication, installation, model inference,
  and host acceptance. Never claim a run you did not perform.
- Keep `index.html` offline-capable and keyboard accessible. No external scripts,
  fonts, embeds, tracking, or credential forms. Never commit a generated login
  helper, private device details, conversations, or deployment journals.
- Run `python3 -B scripts/check_public_content.py` and `git diff --check`.
  Inspect desktop/mobile layouts and interactive controls after visual changes.

See `CONTRIBUTING.md` for contributor workflow and `docs/runtime.md` for pins.

For hosted access documentation, keep `README.md`, `docs/getting-started.md`,
`hosted-guide.html` and `start-here.html` consistent. Use the invitation's site;
the general/UVM addresses are linked in the hosted guide. Request access is an
interim form, not automatic account creation or an implemented invitation API.
Keep explanations of sign-in and media recovery user-facing. Runtime settings,
backup paths, operator commands and deployment evidence belong in the private
deployment repository, not this public site. The frozen download image manifest
does not identify every currently hosted application's version.

For model or thinking-level questions, start at
[the participant model section](hosted-guide.html#model) and
[facilitator verification](docs/facilitator-guide.md#model-choices-before-a-session).
Use [the contributor ownership guide](CONTRIBUTING.md#maintaining-model-instructions)
to route application, deployment and public documentation changes. Keep defaults,
site exceptions and actual acceptance separate; never infer provider success
from a selectable menu item.
