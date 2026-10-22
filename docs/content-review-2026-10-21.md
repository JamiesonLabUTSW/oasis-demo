# Hosted invitation guidance review — 21 October 2026

Reviewed by Codex for the OASIS demo documentation maintainers.

The README, getting-started guide, hosted guide and standalone Start Here page
now distinguish personal invitation activation from ordinary sign-in. Invited
participants choose their own password, keep the one-time link private and use
the expiry in their email. Existing accounts retain their current password.
Session end dates are conditional on the host announcing one; activation expiry
does not promise a site end date. Agent guidance records the same distinction.

The four entry points also carry Andrew's requested General-demo notice:
demonstration and feature exploration only, no private/confidential/sensitive
uploads, no guarantee of uploaded-data privacy, and an invitation to contact
Andrew about a separate private instance with access limited to the individual
or organization. This notice is scoped to General and makes no security guarantee
for a future private instance. It uses existing layout styles; changed text and
markup were reviewed before updating the HTML inventory hashes.

This is original participant-facing documentation. No real invitation URL,
account, recipient list, credential, private screenshot, operational journal,
institutional material or new demo asset is included. Existing demo content,
licenses, notices, image manifest and interactive tutorial code are unchanged.
The changed HTML text was reviewed before refreshing its inventory hashes.

The currently published four illustrated tours opened in a desktop browser;
pause, step navigation and the example handoff worked. Public entry/guide and
project destinations returned HTTP 200. Local HTML path/anchor validation
covered 85 references without missing targets. These are documentation checks,
not participant activation, authenticated media playback, grading or export
acceptance. This revision still needs PR review, Pages publication and served
content verification before being described as live.

Andrew also requested an encouraging invitation for feedback and feature ideas.
The four entry points welcome suggestions and explain replying to the invitation;
the full guide retains the in-app feedback route. This does not commit to building
every requested feature. The source text was reviewed before refreshing hashes.

## Release review — 22 October 2026

The release review found one remaining unconditional access-end reminder in the
full guide; it now depends on the host announcing an end date. Start Here now
explicitly covers existing accounts and links directly to sign-in help and
feedback. Its longer access, General-use and feedback paragraphs use the
existing 14-pixel navigation text size instead of 12-pixel footnote text.
These are original instructional copy and accessibility adjustments; no new
feature, encounter isolation or authenticated workflow acceptance is claimed.
Changed text and markup were reviewed before updating the two HTML hashes.

Local validation passed for all 39 inventoried files and 113 local link/path
references across the four entry points, including HTML fragment targets.
The full guide and Start Here were inspected at 390 × 844 and 1440 × 1000;
notice text wraps without horizontal overflow, and the direct help link and
sign-in disclosure work. Pages and final served-copy verification remain the
post-merge step. These checks do not establish participant onboarding acceptance.
