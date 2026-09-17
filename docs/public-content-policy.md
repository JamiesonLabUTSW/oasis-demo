# Public content policy

## Admitted demo content

1. **Original synthetic:** fictional notes, criteria, scripts, and illustrative
   answers created for public demonstration. Record authorship/date and confirm
   no private case or proprietary instrument was copied or transformed.
   Synthetic content retains project terms; it is not automatically public domain.
2. **Verified public-domain source:** exact work, creator, source URL,
   item-specific rights evidence, jurisdiction, attribution, and review date.
   A freely accessible page or government domain alone is insufficient.
   Review recordings, rubrics, transcripts, translations, and derivatives separately.

The initial catalog links to external CDC media and stores no copy. Future
downloads, embeds, thumbnails, derivatives, and archives need their own review.

## Excluded

Institutional/proprietary rubrics; vendor instruments; partner packets; real or
de-identified learner/patient records; private recordings/transcripts; screenshots
containing them; secrets; and generated login-helper pages.

De-identification is not synthesis. Rewording a rubric does not establish
original authorship. Public-domain media does not clear a separately authored
rubric. A private synthetic fixture is not automatically cleared for publication.

Apply this to Git history, issues, releases, archives, container contents, and
hosted copies linked as our demos. Third-party code and application UI assets
retain their own notices; they are not automatically public-domain demo media.

Institution-specific materials, when authorized for use, travel separately:
the material owner supplies a private pack manually to named recipients through
an approved private channel. Keep it outside the public installer, images,
catalog, issues, and release assets. Public demo installation must not depend
on receiving a private material pack.

## Inventory and review

Every proposed file must be registered in `content-inventory.json`.
Downloadable demo assets need provenance and SHA-256. Public-domain entries
need item-specific evidence. Run:

```bash
python3 -B scripts/check_public_content.py
```

The guard rejects unlisted/missing files, disallowed categories, incomplete
provenance, and changed asset bytes. It cannot decide whether content or rights
claims are true. Inspect content before refreshing hashes. Containers require
review of exact layers; this CI does not scan remote images. Archives/workbooks
require member, hidden-sheet, and metadata inspection.

Record scope, exclusions, and uncertainty. Keep private evidence private.
If prohibited material is discovered, stop further distribution, notify the
owner privately, and coordinate cleanup of affected surfaces/history and any
necessary credential rotation. Do not repeat it in a public issue.
