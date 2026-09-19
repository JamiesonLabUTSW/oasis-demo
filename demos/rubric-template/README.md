# Rubric template and sample rubric

Two Excel workbooks for the MAPLES rubric upload (`Rubrics → Upload New
Rubric`). Both are lab-authored fictional teaching material with no third-party
content, released under the same academic-use terms as this repository's
[LICENSE](../../LICENSE). They are not validated assessment instruments.
The [hosted guide](../../hosted-guide.html#rubric-template) shows where they
fit in the workflow.

| File | What it is |
| --- | --- |
| `rubric-template.xlsx` | Blank template: the three sheets and the full column set, with one placeholder row |
| `documentation_quality_note.xlsx` | Filled example: the six-criterion note rubric the hosted demo loads as **Trial documentation quality** |

## Sheets

- `_metadata` — four label/value rows: `Name`, `Description`, `Version`,
  `Context`. Describe what the rubric assesses and the setting it assumes.
  The upload dialog also asks for the display name shown in Rubrics.
- `_mapping` — one row per station: `Station`, `Activity`, `Case`, `Context`.
  `Station` must match a station sheet name. The sample lists three fictional
  sample cases under a `Starter Assessment` activity; when your group's
  activity/case is not listed here, the app shows **Station mapping required**
  and you choose **Confirm Mapping** in Grading.
- One sheet per station — `Station1` in the template, `Documentation` in the
  sample. Rename the sheet to match your station if you fill in `_mapping`.

## Station sheet columns

`ItemKey`, `Mode`, `Section`, `QuestionText`, `Response1`, `Response2`,
`Response3`, `AdditionalContext`, `Technique`, `Purpose`, `MaxRating`.

- `ItemKey` — unique within the station; keep it stable across versions so
  runs can be compared row by row.
- `Mode` — `Note` for a written note. The in-app **User Guide → Rubric Format
  Guide** describes the other modalities.
- `Section` — a short grouping label for the item.
- `QuestionText` — what the evaluator should assess.
- `Response1`, `Response2`, `Response3`, … — one description per score level,
  in order, at least two nonblank and with no gaps. Add later levels as new
  columns in sequence.
- `AdditionalContext`, `Technique`, `Purpose`, `MaxRating` — optional. The
  template shows them; the sample omits them.

## Min Score rule

**Min Score** in the upload dialog sets the score for `Response1`; each next
response receives the next integer. The sample uses **1**, so its scores run
from 1 to 3. For a 0/1 rubric, set Min Score to **0**. Do not add "N/A"
placeholder score levels.

## Provenance

Both workbooks were exported unchanged from the OASIS project's sample rubric
set (created 2026-02-19). Every sheet, cell and package part was inspected
before publication: no hidden sheets, comments, macros, embedded media or
personal metadata. SHA-256 values are recorded in
[content-inventory.json](../../content-inventory.json).
