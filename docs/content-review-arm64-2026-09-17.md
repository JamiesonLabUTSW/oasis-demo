# ARM64 content and evidence review — September 17, 2026

## Exact scope and current availability

This review binds application `4abb0bb242228c528ef23876dd8746f3470882b3`
and the five core `linux/arm64` package references in
[images-arm64.json](../images-arm64.json). They resolve to four distinct native
runnable manifests and 52 unique layers. Optional MCP is excluded.

| Item | Status |
| --- | --- |
| Exact image content review | Scoped PASS; limitations below |
| Third-party evidence/source snapshot | `EVIDENCE_ASSEMBLED`; final archives verified |
| GitHub release assets | `PREPARED_NOT_PUBLISHED` |
| Public ARM64 images | `PREPARED_NOT_PUBLISHED` |
| Fresh-recipient Mac installation and acceptance | Pending; separate assisted handoff |

These statuses are independent. This review does not establish an anonymous
image download, an installation, a model run, or recipient acceptance.

## Image content review

The review verified manifest/config identities, compressed layer hashes and
sizes, uncompressed layer identities, regular-file inventories and nonempty
history layers. Archives were inventoried with bounded recursive inspection;
link targets were recorded without following them. The admitted synthetic
example workbook matched its exact application-source bytes and was reviewed
as workbook content, separately from the secret scanner.

All retained scanner findings were resolved against exact source or upstream
provenance. These included public signing metadata, dependency checksum rows,
NumPy test fixtures and a Python bytecode file falsely recognized as a ZIP.
No unresolved finding remains in this bounded review. Resolution of a specific
source-matched finding does not authorize a general scanner exclusion.

The review excludes optional MCP and its uncleared reference workbooks. Runtime
volumes, databases, learner data, operator credentials and operator model caches
are not distribution inputs. Institutional rubrics and private demonstration
materials remain outside this public release.

### Review limits

- Pattern-based secret scanning uses built-in path/value allowlists and skips
  some dependency, document and recognized binary classes.
- First-party Go binaries and uv helpers received additional ASCII and UTF-16
  string checks. Other upstream binaries were inventoried and reviewed for
  provenance, not exhaustively string-scanned.
- Recursive archive inspection was bounded to four levels and decoding to five.
- This is content hygiene and provenance review, not proof that every possible
  secret is absent, a vulnerability assessment, or legal certification.

## Third-party companion

The [source and license manifest](third-party/4abb0bb2-arm64-r1/SOURCE-LICENSE-MANIFEST.json)
and [companion README](third-party/4abb0bb2-arm64-r1/README.md) describe the immutable
snapshot. The intended [release page](https://github.com/JamiesonLabUTSW/oasis-demo/releases/tag/4abb0bb2-arm64-r1)
is not claimed available until publication is separately verified.

| Prepared release asset | Bytes | SHA-256 |
| --- | ---: | --- |
| `oasis-arm64-4abb0bb2-third-party-evidence-r1.zip` | 7,067,501 | `c9827ccb1afcb0aa028668931f0fe70111273b4cf03266f2bc7edddb77b12e56` |
| `oasis-arm64-4abb0bb2-third-party-evidence-r1-sources.zip` | 193,502,505 | `cf6706e72241752add1a433ff25d7a8893dec7cd8be61a7ccad552295a62c82a` |

The evidence ZIP has 223 members: four SPDX and four Syft SBOMs, four discovered
package/license reports, build recipes and patches, source indexes, notices and
supporting documentation. The source ZIP has 62 members: 58 verified upstream
source archives plus the README, snapshot manifest and two indexes. Neither ZIP
contains OCI layers, application Git history, installed native executables,
operator model weights/caches, credentials, runtime databases or learner data.

Independent review checked ZIP integrity, every outer member name/type, exact
allowlists, byte identities and all 58 source payload hashes. Earlier in-memory
inspection covered every member and link in those unchanged source archives;
no code, source-support model or test payload was executed. Public SBOM copies
omit private registry/acquisition metadata while preserving package, image and
layer identities and consistent SPDX relationships.

Third-party source, manuals, notices and upstream test fixtures keep their own
licenses. They are not original synthetic or public-domain OASIS demo assets.
Source archives can contain upstream test media, fonts, certificates and
source-support models, including VMAF assets. OASIS project restrictions do not
relicense these components. The exact FFmpeg binaries use GPLv3-or-later settings.

The recipe index distinguishes 51 included source references, one disabled FDK
reference whose source/notices are excluded, and one reference-only libmysofa
1.3.3 source. That exact upstream tag/archive was unavailable; no other source
version was substituted. Included notices explicitly distinguish an exact-version
Debian `1.3.3+dfsg-1` copyright record from the identical notices in adjacent
upstream releases. Alpine recipe correspondence is reconstructed from recorded
versions and official history; the builder package database was not retained.
Package `NOASSERTION` entries remain visible. Transitive source completeness,
complete build provenance and legal completeness are not certified.

See [runtime details](runtime.md) for publication and installation boundaries.
The existing AMD64 manifest, project license and third-party notices are unchanged.
