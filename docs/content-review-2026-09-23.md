# Animated starter guide — content review, 23 September 2026

The owner approved publication of the illustrated starter guide and its four
separate note, audio, video, and transcript tours. Reviewed the complete HTML,
CSS drawings, authored snippets, scoring illustrations, and JavaScript before
admitting the generated bundle to this public repository.

## Content and provenance

The short note sentence, dialogue exchanges, illustrative criteria, suggested
scores, and recording timestamps were created expressly for this guide with
AI assistance on 23 September 2026. They are fictional teaching illustrations,
not quotations from learner records, outputs of grading, validated instruments,
or extracts from the CDC recording. No private or institutional material was
copied or transformed. The note, bubble, video, headphone, and waveform drawings
are CSS artwork authored for the guide. No recording, real transcript, screenshot,
logo, externally loaded image, workbook, credential, or account identifier is
included. Existing root LICENSE terms apply; this is not a public-domain grant.

## Files and behavior

- `start-here.html`: standalone, offline-capable public entry point.
- `assets/starter-guide.js`: self-contained markup, styles, illustrations and
  controls. Uses a shadow root to isolate its styles. No external libraries,
  fonts, embedded media, tracking, storage access, or API/provider calls.
- `index.html` and `hosted-guide.html`: links to the new quick start.

The bundle also supports an educational help overlay in hosted MAPLES sites.
There it opens from Start here and can navigate through the site's existing
Grading link. This public page does not choose a private site, accept login
credentials, claim to preselect a rubric/group, or run an assessment. Its sample
names are explanatory references already used by the hosted guide. Actual
examples and model access vary by site. Audio-only provisioning is not claimed.

Four five-second chapters have pause/play, next/previous, replay and format
selection. Reduced-motion preferences suppress animation and initial autoplay;
manual chapter navigation remains available. Illustrations label their fictional
status, and simulated grading time is distinguished from real execution.

## Evidence scope

Inventory, syntax, desktop/narrow layout, modal controls and keyboard navigation
are checked for this static publication. Host runtime installation and account
acceptance are separate; no new inference is needed or claimed. Frozen image
manifests, LICENSE, and THIRD_PARTY_NOTICES are unchanged.

## Modality colors and icons revision

At the owner's request, note uses MAPLES amber/yellow, transcript green, video
purple, and audio blue across cards, tours, format selectors and next steps.
The palette follows `ResultItemCard.tsx`; exact Lucide StickyNote, Languages,
Film and Headphones paths follow the MAPLES encounter/group UI. Four small
SVG glyphs were reviewed from the installed `lucide-react` 0.563.0 package.
Their ISC and applicable Feather MIT notices are preserved in the bundle and
THIRD_PARTY_NOTICES. They are licensed application UI code/assets, separate
from the original synthetic teaching illustrations described above. The
palette values are the corresponding Tailwind 4.1 theme scales used by MAPLES.
No demo data, examples, grading behavior or external dependencies changed.
