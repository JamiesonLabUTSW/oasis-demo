# OASIS demo library

Start with a small example, understand the review workflow, then arrange an
assisted OASIS/MAPLES installation for your computer.

**Public demo content is original synthetic material or a source-specific,
verified public-domain reference.** Institutional rubrics, private recordings,
partner packets, real learner notes, and credentials do not belong here.

## Start here

**First read [Start here: choose your path](docs/audience-guide.md).** It explains
the shared workflow and vocabulary, then points users, teachers, developers and
agents to the right next guide.

| You want to… | Go here |
| --- | --- |
| Learn about the OASIS project | [OASIS project site](https://jamiesonlabutsw.github.io/oasis/) |
| Read and cite the technical report | [OASIS preprint on arXiv](https://arxiv.org/abs/2609.09180) |
| Explore the library | [Demo start page](index.html) — save the repository and open locally |
| Try a short notes exercise | [Three fictional notes and an original practice rubric](demos/synthetic-notes/README.md) |
| Find a public-domain recording | [CDC conversation: source and attribution](demos/cdc-conversation.md) |
| Install OASIS/MAPLES | [Getting started](docs/getting-started.md) — assisted package required |
| Run a workshop or plan a site pilot | [Facilitator guide](docs/facilitator-guide.md) |
| Report a problem | [Support](docs/support.md) |
| Contribute as a developer or agent | [Contributing](CONTRIBUTING.md) · [Agent instructions](AGENTS.md) |

The HTML page works offline without a server, account, external fonts, or
analytics. GitHub displays its source; open the downloaded `index.html` in a
browser. There is currently no hosted Pages URL advertised here.

The [OASIS project site](https://jamiesonlabutsw.github.io/oasis/) provides the
broader project context and guided tours; the
[arXiv preprint](https://arxiv.org/abs/2609.09180) provides the technical report
and citation. A connection to UT-REAL is planned; its public link will be added
when that connection is ready.

## Demo catalog

| Demo | Content | Ready now | Further qualification |
| --- | --- | --- | --- |
| [Notes review practice](demos/synthetic-notes/README.md) | Three newly authored fictional notes; three original criteria | Read, score by hand, reveal illustrative answers; download text | OASIS import mapping and a recorded grading/review/export run remain pending |
| [CDC conversation](demos/cdc-conversation.md) | External CDC recording, public domain in the United States per its file-specific record | Source link, attribution, provenance | Host's tested media/model route and an independently cleared rubric; no media or rubric bundled |
| [Future site pilot](docs/facilitator-guide.md#site-pilot-template) | Synthetic content first | Reusable planning/acceptance template | Named host, verified package, local rehearsal, and separate governance for later institutional data |

The practice rubric is not a validated instrument. Its answers are authored
examples, not model results.

## Installation status — September 17, 2026

| Computer | Image selection | Status |
| --- | --- | --- |
| Windows Intel/AMD | d40f1955 / Linux AMD64 — [manifest](images.json) | Five public application images; anonymous download and hashes verified |
| Apple Silicon Mac | 4abb0bb2 / Linux ARM64 — [prepared manifest](images-arm64.json) | **Prepared, not published:** exact-content review passed; public copy and anonymous verification pending |

Both selections use the separate `ghcr.io/jamiesonlabutsw/oasis-demo/`
namespace. Use the selection supplied with your matching kit.

- **Assisted:** matching Compose/bootstrap kit supplied separately by your host.
  Pulling images or cloning this repo does not install the stack. There is no
  general public installer or complete public release ZIP here yet.
- **Windows Intel/AMD:** the assisted route uses Ubuntu/WSL2 and Docker Desktop.
  Each recipient still needs installation, login, and retained-restart checks.
- **Apple Silicon:** request the matching assisted Mac package. Fresh-recipient
  installation, login, sample visibility, and retained restart remain to be proven.
  The prepared ARM64 manifest does not yet establish public image availability.
- **Models:** weights, credentials, and a verified fully local inference
  configuration are not included. Stack startup does not prove offline readiness.

Optional MCP and its unresolved reference materials are excluded. Institutional
rubrics, private recordings, learner data, and workshop packets stay outside
public images and kits; any authorized material handoff is separate.

[Getting started](docs/getting-started.md) · [Runtime details](docs/runtime.md) ·
[Published ARM64 source/license companion](docs/third-party/4abb0bb2-arm64-r1/README.md)
([verified availability](docs/third-party/4abb0bb2-arm64-r1/PUBLICATION.json))

## Public content and terms

[Content policy](docs/public-content-policy.md) and
[content-inventory.json](content-inventory.json) record what is admitted and why.
Run `python3 -B scripts/check_public_content.py` before proposing a change.
The check enforces the inventory and asset hashes; a person must still review
content and provenance. [Review record](docs/content-review-2026-09-16.md).

The unchanged [LICENSE](LICENSE) governs OASIS code and original repository
content: academic research use only, with commercial use prohibited. Public
download does not make the software OSI open source or synthetic content public
domain. External public-domain material retains its own status.
[THIRD_PARTY_NOTICES](THIRD_PARTY_NOTICES) records component notices.

These are academic demonstration materials and unsigned frozen images, not a
production release, medical device, or independently validated assessment system.
