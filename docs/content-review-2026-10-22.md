# Participant guide design review — 22 October 2026

Reviewed by Codex for the OASIS demo documentation maintainers, with independent
Claude Opus 5.5 (high), Gemini 4 Argon (high) and Codex design reviews of public
source and actual desktop/mobile screenshots. The two final external reviews
returned “ready with minor follow-ups”; the remaining concrete layout,
navigation and accessibility findings were corrected and checked in the browser.
These are design reviews, not proof of authenticated application behavior.

## Reviewed changes

- Start Here has one navigation header, a visible General demonstration/data-use
  notice including the private-instance contact route, and an activation/help
  disclosure. Existing-password and conditional activation-expiry instructions
  remain. Feedback follows the exercises. Same-site guide links use the same tab.
- Standalone exercise transitions scroll the document to the new content and
  focus its heading. The embedded guide retains its dialog-scroll behavior and
  existing capability/authentication checks. No account, grading or model request
  was added.
- Helper text and tour controls have larger, darker type. Visible walkthrough
  labels match their accessible names. Autoplay captions do not continually
  announce; pause/play labels are explicit. The real-run timing caveat is in the
  accessible tour description. Mobile illustrations no longer collide with their
  source badges, and chapter progress lines align when labels wrap.
- The full guide uses a balanced two-column exercise grid and distinguishes the
  General data-use notice from invitation logistics. Rubric authoring is directly
  linked; optional installation guidance follows the participant workflow.
- Rubric authoring has task jump links, advanced model/activity help after the
  core workflow, and stacked mobile comparison/checklist tables. Save, Accept
  and Create consequences remain visible. Explicit table semantics are retained;
  unnecessary keyboard stops on non-scrolling table wrappers were removed.

All changed source, including the serialized HTML/CSS inside starter-guide.js,
was inspected before updating inventory hashes. Changes are original instructional
layout, navigation and accessibility work. No private records, screenshots,
credentials, operational evidence, new media, copied rubric or new instrument
were added. Existing license, third-party notices and image manifest are unchanged.

## Validation and limits

JavaScript syntax and whitespace checks pass. Local path/fragment checks cover
149 references across six entry/source pages. Desktop 1440 × 1000 and mobile
390 × 844 layouts were inspected; the three guides also reflow at 320 pixels
without document-level horizontal overflow. Browser checks covered the lower
Audio Try button, return to all examples, tour pause and step selection, tour
handoff, Escape with launcher focus restored, activation disclosure, the help
link and rubric task anchors. The four mobile tour progress lines share the same
vertical position after the final correction. This is a focused visual and
interaction review, not a complete assistive-technology certification.

The publication gate is the protected inventory check followed by Pages build
and exact served-byte verification. Participant activation, real media playback,
grading, export and host-release acceptance remain separate responsibilities.
No new application deployment or encounter-isolation claim is made here.
