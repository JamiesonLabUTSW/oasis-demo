# Draft, enhance and adapt a rubric

Use this guide with your invited hosted MAPLES account. Start from an original
practice rubric or material your host has cleared for the session. Keep a named
copy of the source when experimenting, and review the resulting rubric before
using it to grade.

## Choose the right action

| Your aim | Action | When a saved rubric changes |
| --- | --- | --- |
| Write a new rubric or revise an unsaved draft | **Wayfinder** | Only when you choose **Save rubric** |
| Improve wording or scoring anchors in an existing rubric | **Enhance** | When you **Accept** a suggestion or explicitly accept the selected changes |
| Adapt an existing rubric to another scenario | **Transform** | **Create Transformed Rubric** generates and saves a new rubric; inspect it afterward |
| Make a precise edit without an AI request | Make a copy, then edit or upload your revised workbook | When you explicitly save or upload the edit |

The authoring model is configured by your host. On sites with **GPT-6.1 Sol at
high reasoning** enabled, Wayfinder drafting/refinement and Enhance/Transform
use that specialist. The model you select for a grading run is a separate
choice. High reasoning is a request setting, not a guarantee that every proposed
criterion or score is correct. Ask your facilitator to confirm the site's
actual authoring setup if it matters to your comparison.

## Give the model a specific job

State the purpose, intended learner or task, evidence format, number of criteria
and score range. Explain what must remain unchanged and what you want improved.
For an existing rubric, prefer one focused change at a time so you can assess
its effect. Avoid adding real participant or patient information to a prompt.

This newly authored fictional example concerns a desk-organizing exercise:

> Draft six criteria for reviewing a written account of organizing a study
> desk. Include a criterion for documenting the choice to use a timer or not.
> Use Note evidence and scores 0, 1 and 2. Assess what the account documents,
> not whether the person is tidy. Keep each criterion focused on one
> observable feature. Explain how to score omitted information, and make the
> three anchors mutually exclusive. Return a draft for my review.

For a refinement, identify the item and the intended change:

> Keep the item IDs, order, evidence format and score range. Revise only the
> timer-setup criterion so that a documented decision not to use a timer is
> distinct from an account that never mentions a timer. Return the complete
> revised draft for review.

These are instructional examples, not validated criteria or recorded model
outputs. Use only evidence that the selected format can support: a note shows
what was documented; a transcript shows words; silent video cannot establish
what was said.

## Wayfinder: draft, inspect, refine, save

1. Open **Wayfinder**, describe the task and submit once. Allow the request to
   finish; a large rubric can take several minutes.
2. Read the preview from beginning to end. Check every item and its numeric
   score labels. Open **Exact YAML** when you need the complete underlying text;
   **Copy YAML** lets you keep your own draft copy.
3. To revise it, use the card selected for refinement, or choose **Select for
   refinement** on the intended card. Ask for a specific correction and check
   the new complete draft against the previous one.
4. Choose **Save rubric** only on the version you intend to keep. Confirm
   **Saved to your rubrics.**, then use **View saved rubric** and inspect the
   saved criteria and score range.

Preview and refinement do not save a rubric. Unsaved drafts and chat history
can be lost when the page reloads. A saved rubric remains available in your
rubric inventory. Do not assume that saving a later draft removed an earlier
saved version; use clear names and inspect the inventory.

## Enhance: compare each proposed change

Open **Enhance** on the intended rubric and choose the review focus. Select
**Generate Enhancements** once. Compare **Current rubric** with **Proposed
enhancement** and read the stated reason. The explanation is a proposal you
must evaluate, not proof that the change is better.

Check that each suggestion preserves the construct you meant to assess. Use
**Accept** for a reviewed change or **Reject** for one you do not want. If you
use a control to accept several suggestions, review all of them first. Reopen
the rubric and verify the saved result. Generating suggestions by itself does
not apply them. Work on a copy when you want to retain the original wording
for a comparison.

## Transform: create a separate rubric

Open **Transform** on the source rubric. Enter a distinct **New rubric name**,
the **Target station** when needed, and a clear **Target scenario**. Explain
which features should carry over and which should change.

**Create Transformed Rubric** is the creation action: it generates and saves a
new rubric in the same request. It does not offer Wayfinder's separate draft
preview before saving. The source rubric remains available. After the success
message, open the new rubric and review its wording, IDs, stations, evidence
format and scoring anchors before using it. A new scenario can require changes
to mappings or assumptions that the model did not recognize.

## Review the substance, not just the formatting

| Check | What to look for |
| --- | --- |
| Purpose | Each criterion measures the intended feature, without introducing a new task or hidden requirement. |
| Evidence | A reviewer can point to evidence in the chosen note, transcript or recording. Omission does not prove an action occurred. |
| Score anchors | The same observation cannot satisfy two different scores. Boundaries are explicit and ordered. |
| Missing versus negative | An explicit statement of “none” is distinguishable from missing documentation where that distinction matters. |
| Preservation | Required item IDs, order, item count, station, evidence format and score range survived the edit. |
| Fairness and usefulness | Wording is relevant to the task and does not reward irrelevant personal attributes or unsupported assumptions. |
| Saved result | The rubric you reopened matches the version you approved. |

For example, “no timer was used” documents a decision; silence about a timer
does not. Decide whether that decision meets the criterion's purpose, then
place it in exactly one scoring anchor. Do not automatically reward all
negative statements or infer an assessment from an omission.

Try the revised rubric on a few host-approved fictional examples and compare
human interpretations before broader use. Successful generation, parsing or
saving does not establish educational validity or grading accuracy.

## If a request fails or the outcome is unclear

Keep the page open and note the action, rubric name, approximate time and
displayed Trace ID or sanitized error. Avoid repeated clicks: a timeout does
not establish that provider work or billing stopped.

- **Draft/refinement failed:** no new rubric is saved by that generation step.
  Keep any earlier draft and ask your facilitator before repeating the request.
- **Save outcome unclear:** use **Check again** on the draft card and
  **Inspect existing rubric** when available. These actions only read your
  rubrics; they do not save another copy. Compare the saved content with your
  draft: a matching name alone does not prove the content matches. If no match
  appears, the original save may still be finishing. Keep your draft and ask
  your facilitator to check before saving again.
- **Enhance outcome unclear:** reopen the source rubric and check which
  suggestions, if any, you had explicitly accepted.
- **Transform outcome unclear:** check for the new name before creating
  another transformed rubric.
- **Model or credential unavailable:** ask the facilitator to check access
  for your account. Never paste an API key into Wayfinder, feedback or a public
  support report.

Share only the support details your host needs. Keep rubric content, account
information and provider receipts in the host's approved private channel.
See the [participant guide](../hosted-guide.html#help),
[facilitator checks](facilitator-guide.md#model-choices-before-a-session) and
[support guide](support.md).
