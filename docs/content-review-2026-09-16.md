# Public content review — September 16, 2026

## Existing repository

Initial public commit `ad6b306843690476a374f7561991e1be7a5b06f0` contains only
README, LICENSE, THIRD_PARTY_NOTICES, and images.json. Its complete existing Git
history was inspected: no cases, rubric files, recordings, transcripts, or notes.

## Frozen images: evidence and limits

The publication review inspected configuration/history and application COPY-layer
payloads at the manifest's exact digests. The maintainer's record reports no
credential paths in inspected payloads. Scanner matches in Python configuration
were resolved as upstream public GPG key IDs.

Bundled `maples/src/rubric_zipper/ExampleRubric.xlsx` was inspected as structured
workbook XML at the exact application commit. Metadata labels it synthetic
teaching content; two case sheets contain generic questions. Optional MCP
contains reference workbooks without established public-release status; it was
excluded and remains private.

This summarizes a scoped publication review, not a new exhaustive audit of every
layer, dependency right, or downstream installation. Manifest changes require
new artifact review.

## New public library

- Notes, criteria, and answers under `demos/synthetic-notes/` were authored afresh
  for this public library: a fictional routine-planning conversation. No private
  record, institutional rubric, instrument, or collaborator packet was copied.
- Scores are authored examples. No model run or OASIS import is claimed.
- CDC source links, file-specific rights, and agency policy were rechecked.
  See [public evidence](../demos/cdc-conversation.md). No private accompanying
  rubric, transcript, audio derivative, or recording was copied.
- Source-video public-domain status is recorded for the United States, not for
  a whole private demonstration package.
- The site contains original HTML/CSS, system fonts, no external media, analytics,
  scripts, forms, or credentials.
- LICENSE, THIRD_PARTY_NOTICES, and images.json are unchanged.

The inventory guard checks proposed repository files. Hashes do not establish
permission; content/provenance review remains necessary for future changes.

## Owner clarification and distribution boundary

The owner explicitly confirmed that original synthetic examples and verified
public-domain materials are both allowed. Synthetic content keeps its existing
terms; it is not relabeled public domain. Authorized institution-specific
materials must travel separately in private, manually supplied recipient packs.
The public library neither contains nor requires those packs.

## Verification for this change

- Inventory and hashes: 22 proposed files registered; original license, notices,
  and image manifest match their initial bytes.
- Negative checks: unlisted attachment, changed demo bytes, missing item-specific
  rights evidence, demo mislabeled as documentation, and escaping path rejected.
- 66 local file/section links resolved; displayed notes match the text downloads;
  authored CSV score totals are internally consistent.
- Gitleaks scanned the proposed directory with redacted output: no findings.
- Browser inspection: desktop and narrow layouts, answer reveal, and no
  horizontal overflow in the mobile answer table. The page has no external
  scripts, embeds, media, or forms.

No installation, transcription, model grading, or institutional data handling
was performed by this website change. GitHub Pages was not enabled.

## Related-project navigation

Added the public OASIS project site at
[jamiesonlabutsw.github.io/oasis](https://jamiesonlabutsw.github.io/oasis/) to the
start-page navigation and README. The URL matches the public repository's
homepage and GitHub Pages configuration; its live page identifies OASIS and
MAPLES. UT-REAL is noted as a planned connection with no speculative link or
claim of deployment readiness. This edit adds navigation only, not new demo
content or embedded assets.

## Visual refresh and OASIS theme alignment

The demo page now follows the public [OASIS project site's](https://jamiesonlabutsw.github.io/oasis/)
visual palette: dark blue-green navigation, warm cream/sand surfaces, teal
actions, gold/coral accents, and system sans-serif type. The palette and type
were checked against the live site's rendered styles and public stylesheet.
The layout and inline SVG illustrations were authored for this repository;
there are no added image files, external fonts, scripts, or media dependencies.

The opening uses the existing synthetic Note A with highlighted evidence,
explicitly labeled an authored illustrative example. Demo cards have distinct
icons, notes appear side by side on wide screens, and setup has a separate
dark section. All existing link destinations and downloadable note text are
retained. Decorative icons are hidden from assistive technology; keyboard
focus and reduced-motion preferences are supported.

Validation includes wide/narrow browser inspection, keyboard answer disclosure,
local link checks, note/download comparison, and the public-content inventory.
The reviewed HTML hash is refreshed after inspecting this presentation change.

## Project and paper cross-links

Added visible OASIS project and arXiv links beside the demo introduction, in the
footer, and in the README. The canonical paper URL is
[arxiv.org/abs/2609.09180](https://arxiv.org/abs/2609.09180); its title and project
link were verified on the live abstract page. These are navigation links,
without copied paper text, media, or new downloadable content.

The companion OASIS-site change points back to the existing public
`oasis-demo` repository. A dedicated demo Pages URL is not yet live; update that
return destination after hosting is published and verified, rather than adding
a currently broken site link.
