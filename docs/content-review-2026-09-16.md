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
