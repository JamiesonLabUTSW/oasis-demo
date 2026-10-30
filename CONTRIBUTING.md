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
login helper. The site has no build step or backend. GitHub Pages serves the
public `main` branch at the repository root; `.nojekyll` preserves its static
files. Changes reach the site through the checked pull-request workflow.

## Runtime and support

Runtime/image/platform changes require separate release evidence. Preserve the
existing license/notices and frozen image selection during site edits.
Keep actual site journals in the host's approved private workspace.
Follow the [support guide](docs/support.md) for public reports.

## Acceptance feedback and workflow improvements

After a walkthrough, consider another plausible route a first-time or
experienced educator might take. Check the intended job: can they find their
grades and source evidence, retain a review, and obtain an export that agrees
with the saved result? Report only what was actually observed; available
instructions or controls do not prove a successful grading run.

Capture the user goal, expected route, actual result, smallest reproduction,
impact and one testable improvement criterion. Distinguish a defect, usability
friction, proposed idea, evidence gap or useful alternate path. Search existing
reports and follow [support](docs/support.md) to link one canonical item with a
named next owner. Decision, implementation and verified retest are separate.
Public reports use original cleared examples and public-safe descriptions;
private records, credentials, screenshots and runtime evidence stay with the
authorized private operator.

Maintainers with private access use the
[shared computer-use playbook](https://github.com/JamiesonLabUTSW/oasis-internal/blob/fd5450475b303d34e4d8fbfec61a1d6958594e1d/docs/internal/user-acceptance/README.md)
and its workflow/session templates. It complements participant guides and
keeps reusable testing instructions in one place. Private access is required;
public contributors can use the feedback instructions above without it.
See the [content review](docs/content-review-2026-10-29.md) for this change.

## Hosted access documentation

When an approved hosted address or access path changes, update the README,
getting-started page, hosted guide and standalone Start here links together.
Tell participants to use the site in their invitation and their assigned
account. Explain redirects, a possible fresh sign-in and reopening an encounter
for a fresh media link without exposing deployment settings or signed URLs.
Keep the approved Request access wording and responder destination consistent;
do not publish form editor links or describe intake as account provisioning.

Review the changed content before updating inventory hashes. Validate local
links and HTML anchors, check the changed guide on desktop/mobile, and inspect
public links without submitting access requests. After merge, confirm Pages
completed and the served guide matches the reviewed bytes. Deployment and
authenticated playback acceptance are separate checks recorded privately.

## Maintaining model instructions

The participant contract is [the model section](hosted-guide.html#model);
[facilitator checks](docs/facilitator-guide.md#model-choices-before-a-session)
separate menu availability from inference acceptance. Keep README, getting-started,
Start here and that section linked and consistent when labels or defaults change.
Verify UI wording against the application and describe site exceptions explicitly.
Application alias binding and provider validation belong in `oasis-internal`;
site catalogs, Azure endpoints, credentials and live journals belong in the private
`gcp-oasis-deploy` repository. Do not copy their operational records here.
A hosted feature does not change this repository's frozen image manifest.

Rubric authoring instructions live in [the dedicated guide](docs/rubric-authoring.md).
The offline HTML page `rubric-authoring.html` is rendered from that Markdown
source; review and update both copies and their inventory hashes together.
Keep authoring-model configuration separate from grading presets. Preserve the
different creation boundaries of Wayfinder, Enhance and Transform. Link changes
from the participant, getting-started and facilitator routes, and review any new
fictional prompt as original public content before updating its inventory hash.
