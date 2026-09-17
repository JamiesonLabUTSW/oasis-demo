# Exact ARM64 third-party evidence — 4abb0bb2 r1

The exact SBOM, source and notice evidence is assembled. This immutable evidence
snapshot does not track later image/release availability; consult the public
distribution page and its publication receipt for that status.

Together the evidence ZIP and source ZIP bind five intended public packages to
four exact linux/arm64 image manifests. The evidence ZIP contains SPDX/Syft SBOMs,
discovered package license reports, upstream FFmpeg build/version documentation,
build patches and license texts. The sibling source ZIP contains the verified
upstream source archives. Paths to SBOMs/notices in either manifest refer to the
evidence ZIP. Image bytes are not included or modified. See
SOURCE-LICENSE-MANIFEST.json for exact bindings.

## License and source boundaries

Third-party source code, documentation, test fixtures and notices retain their
upstream terms. They are source materials, not OASIS demo inputs and not claimed
to be original synthetic or public-domain data. OASIS project restrictions do
not replace these licenses. FFmpeg's exact binaries use GPLv3-or-later settings.
The source ZIP includes verified archives listed in sources/archive-inventory.json.
FreeType's ft2demos source is paired with its same-version FreeType archive, whose
docs/FTL.TXT and docs/GPLv2.TXT supply the referenced license terms.
The source-location index distinguishes included archives, exact references whose
bounded downloads failed, and disabled FDK codec sources excluded from this
companion. Selected copyleft source archives and associated build/notice materials
are included. The unavailable libmysofa1.3.3 reference is accompanied by the
identical upstream notice from adjacent v1.3.2/v1.3.4 releases, explicitly
labeled as adjacent-release evidence rather than exact missing-tag verification.
The version-specific Debian1.3.3+dfsg-1 copyright record separately supplies
upstream/component author/license notices and documents excluded test datasets;
it is downstream notice evidence, not a replacement source archive.
Package-level NOASSERTION entries remain visible; this evidence
does not certify legal completeness or the provenance of every transitive input.

The private registry namespace, acquisition paths and raw image config were
removed from the public SBOM copy while retaining image/layer/package identity.
SPDX identifiers and relationship endpoints were transformed consistently.
Original reports and a before/after hash receipt remain with the operator.

Historical Alpine recipes are bound to official3.20 snapshot
03eb45c3b90fd9b227de93d316ed7b74f322ca8a preceding the source image build.
Recorded library versions match the relevant recipes; the discarded builder
package database prevents claiming direct build-provenance verification.

No application Git history, learner data, runtime volumes, login helpers,
credentials, operator Gemma/Whisper weights or model caches, installed native
executables or OCI layers are included. Source archives may include upstream
test media, certificates and source-support models (including VMAF assets);
these remain third-party source fixtures under upstream terms and are not
OASIS demo data. No source-support model/test payload was executed.
