# OASIS demo library

Start with a small example, understand the review workflow, then join an
invited hosted session or arrange an assisted OASIS/MAPLES installation.

**Public demo content is original synthetic material or a source-specific,
verified public-domain reference.** Institutional rubrics, private recordings,
partner packets, real learner notes, and credentials do not belong here.

## Start here

| You want to… | Go here |
| --- | --- |
| Learn about the OASIS project | [OASIS project site](https://jamiesonlabutsw.github.io/oasis/) |
| Read and cite the technical report | [OASIS preprint on arXiv](https://arxiv.org/abs/2609.09180) |
| Explore the library | [Demo website](https://jamiesonlabutsw.github.io/oasis-demo/) · [Offline start page](index.html) |
| Join the hosted MAPLES demo | [Participant guide](https://jamiesonlabutsw.github.io/oasis-demo/hosted-guide.html) · [Offline copy](hosted-guide.html) — notes, transcript and video practice; personal rubrics, review and export. Use the sign-in link and individual account supplied by your host |
| Try a short notes exercise | [Three fictional notes and an original practice rubric](demos/synthetic-notes/README.md) |
| Find a public-domain recording | [CDC conversation: source and attribution](demos/cdc-conversation.md) |
| Install OASIS/MAPLES | [Getting started](docs/getting-started.md) — assisted package required |
| Run a workshop or plan a site pilot | [Facilitator guide](docs/facilitator-guide.md) |
| Report a problem | [Support](docs/support.md) |
| Contribute as a developer or agent | [Contributing](CONTRIBUTING.md) · [Agent instructions](AGENTS.md) |

The HTML pages work offline without a server, account, external fonts, or
analytics. Read them on the demo website, or download the repository and open
`index.html` or `hosted-guide.html` in a browser. GitHub's code view displays
HTML source. The documentation website and the invited MAPLES application are
separate: a published guide does not mean the trial is open yet.

The [OASIS project site](https://jamiesonlabutsw.github.io/oasis/) provides the
broader project context and guided tours; the
[arXiv preprint](https://arxiv.org/abs/2609.09180) provides the technical report
and citation. The [UT-REAL project](https://ut-real-ai-project-maples.com/)
provides participating-site information, research and MAPLES walkthroughs.

## Demo catalog

| Demo | Content | Ready now | Further qualification |
| --- | --- | --- | --- |
| [Notes review practice](demos/synthetic-notes/README.md) | Three newly authored fictional notes; three original criteria | Read, score by hand, reveal illustrative answers; download text | OASIS import mapping and a recorded grading/review/export run remain pending |
| [CDC conversation](demos/cdc-conversation.md) | External CDC recording, public domain in the United States per its file-specific record | Source link, attribution, provenance | Host's tested media/model route and an independently cleared rubric; no media or rubric bundled |
| [Future site pilot](docs/facilitator-guide.md#site-pilot-template) | Synthetic content first | Reusable planning/acceptance template | Named host, verified package, local rehearsal, and separate governance for later institutional data |

The practice rubric is not a validated instrument. Its answers are authored
examples, not model results.

## Installation status — September 16, 2026

- **Public:** five frozen Linux AMD64 application images in [images.json](images.json),
  anonymously downloadable from `ghcr.io/jamiesonlabutsw/oasis-demo/`.
- **Assisted:** matching Compose/bootstrap kit supplied separately by your host.
  Pulling images or cloning this repo does not install the stack. There is no
  general public installer or complete public release ZIP here yet.
- **Windows Intel/AMD:** the assisted route uses Ubuntu/WSL2 and Docker Desktop.
  Each recipient still needs installation, login, and retained-restart checks.
- **Apple Silicon:** request a separately verified Mac package. This public
  AMD64 manifest is not an ARM64 installation qualification.
- **Models:** weights, credentials, and a verified fully local inference
  configuration are not included. Stack startup does not prove offline readiness.

[Getting started](docs/getting-started.md) · [Runtime details](docs/runtime.md)

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
