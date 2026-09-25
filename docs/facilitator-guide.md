# Facilitator guide

## Hosted workshop handoff

Give participants the [general MAPLES demo guide](../hosted-guide.html) and,
separately, the verified sign-in link and their own credentials. Before sharing
access, verify ordinary login,
the intended sample/group/rubric, one grading run, saved human review and an
opened export. Check two accounts' workspace ownership. Confirm Wayfinder and
media separately before advertising them as available.

Keep the guide reusable across audiences. The invitation supplies the actual
HTTPS sign-in link, access end date, available exercises, model choices, usage
allowance and support contact. Do not route new audiences to another site's
dedicated instance. A published guide does not establish that a demo is live.

Prepare one shared library of approved examples and a starter workspace per
account. Include the fictional notes and, when qualified, the CDC video/audio
and separate transcript exercises. For the latter, verify the saved transcript,
five Transcript criteria, station mapping, one text grade, saved review and
opened export; no new transcription job is required. Identify the exact group
and rubric names in the handoff. Keep a saved presenter result as a fallback.

The transcript and media rubrics assess different criteria. Explain the evidence
each receives and the limits of machine transcription. Use a dedicated instance
for private institutional content; it must not enter the shared practice library.

A persistent **Demo guide** link on the MAPLES sign-in page and in its footer
can open `https://jamiesonlabutsw.github.io/oasis-demo/hosted-guide.html` in a new
tab. The built-in **User Guide** continues to provide general application help.
Publish and check the general guide before enabling the link for a new cohort.
Keep passwords, provider keys, private deployment evidence and generated access
helpers out of this public site.

## Model choices before a session

Use the [participant model instructions](../hosted-guide.html#model) as the
shared explanation of Flash high/medium/low, Sol medium/high/extra-high and Luna
maximum. General and Houston offer these presets; UVM retains its existing
configuration. Confirm the choices in an ordinary participant account's
**Grading → Model Config** for the intended input type. Flash defaults to high.
Opening the menu and cancelling verifies availability without submitting a run.
Saving configuration also does not start grading.

Model availability, successful provider inference, and completed review/export
are separate checks. Rehearse an actual run only within the host's approved
usage; do not describe a menu check as successful grading. Supply a saved result
if the site is offline or a provider is unavailable. Compare the same input and
rubric version when demonstrating model differences, and explain that thinking
levels are not rubric score levels or a quality guarantee. Wayfinder availability
and its assistant model require a separate check.

For a missing choice or provider error, record the site, input type, preset label,
run ID if one exists, and a sanitized error. Contact the site operator; keep keys,
account exports and private evidence out of this repository. Operators maintain
per-site Azure allocations, credentials, rollout receipts and recovery in the
private deployment documentation. New sites need explicit adoption; publishing
this guide does not configure them or update the frozen downloadable images.

## A short first session

1. Explain the loop: note → rubric → suggested evidence/score → human review →
   export. Start with [three fictional notes](../demos/synthetic-notes/README.md).
2. Score before revealing. Find the goal, barrier, and next step in each note,
   then compare the authored examples.
3. Show a rehearsed stack using its compatible synthetic sample. State the
   package and model actually running.
4. Inspect evidence, revise a score if appropriate, save, refresh, export, and
   reopen. Treat disagreements as prompts for review.
5. Give each participant the public catalog and their kit instructions or a
   clear setup-help route.

Keep a rehearsed host available during new installs. Never substitute a private
case packet when a public demo fails. Download, startup, and complete grading
are different milestones.

## Site pilot template

Use this for a later UT-REAL or other site pilot. It does not establish deployment,
institutional data-use approval, or clinical validation. Fill it in the site's
appropriate private workspace.

```text
Pilot label:
Host/contact (private):
Demo objective:
Approved demo ID and synthetic/public-domain input hashes:
Package revision/hash and operating system/architecture:
Model/provider, processing location, and expected cost:
Prerequisite / install / login / retained-restart results:
Grading / human review / export / reopened-export results:
Fallback demonstration:
Open problems and next owner:
Recipient instructions location:
Date and scope of acceptance:
```

Begin with public synthetic content. Actual institutional notes, proprietary
rubrics, private media, and operational identifiers belong to a separately
governed phase, never this public repo, its issues, or demo screenshots.

## Recipient handoff

Provide the exact kit, prerequisites, successful-run checklist, daily commands,
and support contact. Credentials belong in the installer-generated local helper.
Keep device journals privately and publish only generic synthetic reproductions.
