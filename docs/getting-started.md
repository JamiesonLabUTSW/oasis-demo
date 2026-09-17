# Getting started

## Joining a hosted session?

Use the [hosted MAPLES participant guide](../hosted-guide.html) and
[open the hosted demo](https://136-65-236-41.sslip.io). Your facilitator
provides your assigned account privately. Public registration is closed. You need
a browser and internet access; no local installation or personal model key is
required. Start with the prepared group and **Trial documentation quality** rubric.
The guide covers grading, human review and Excel export, followed by
[editing/uploading your own rubric and adding a note with the host](../hosted-guide.html#bring-your-own).
Final browser walkthrough checks are still in progress.

## Cloud hosted or local install?

| Option | Benefit | Tradeoff |
| --- | --- | --- |
| Cloud-hosted demo | Browser access, prepared examples and host-managed model access | Internet, external AI services, shared capacity and a temporary trial |
| Local installation | Control your own OASIS instance, files and configuration | Matching kit, Docker, adequate hardware, maintenance, model setup and any provider costs |

A local installation can still use cloud AI APIs. Fully offline use needs a
separately configured and tested local model with enough hardware.

The installation steps below are optional for hosted participants and are for
people setting up their own computer.

## 1. Try an example

Open the [notes practice](../demos/synthetic-notes/README.md) or `index.html`.
Score three fictional notes against three original criteria, then compare
illustrative answers. No account, installation, or model is needed.

## 2. Get a package matched to your computer

Ask your demo host for the complete kit. This public repository contains the
website, content, notices, and image coordinates, not the installation scripts.

The host should supply the download/access instructions and SHA-256, supported
platform and prerequisites, install/verify/start/stop commands, a compatible
synthetic sample, and the agreed model/provider route and any cost.

Do not substitute commands from another laptop's package. If you have no kit,
[request setup help](support.md); no general public installer is available here
yet. A correctly supplied assisted kit does not require application-source access.

| Computer | Route | Still needs verification |
| --- | --- | --- |
| Windows Intel/AMD | Host-supplied AMD64 kit with Ubuntu/WSL2 and Docker Desktop | Current resources, install, login, sample, retained restart |
| Apple Silicon Mac | Host-supplied Mac kit | Exact native package, model choice, device acceptance |
| Other Linux/Windows ARM | Ask for an explicitly supported package | No general support claim here |

Use your kit's resource checks. Chip names and total RAM do not establish
sufficient free memory, storage, or local-model capacity.

## 3. Install and sign in

In the terminal specified by the package README, verify the download hash,
check prerequisites, review the plan, install, and verify. Stop on failed checks.

The current assisted Windows kit provides `check`, `plan`, `install`,
`verify`, `guide`, `start`, `status`, and `stop` through `oasis.sh`.
Those commands work **inside that extracted kit**, not this repository.

Its `guide` command creates a private local `demo-access.html` with copy
controls for the generated email and password. Open the printed file path.
Keep it on your own computer, outside Git and shared folders; do not upload,
screenshot, or serve it. Follow your specific package's guide/start behavior.

Confirm:

1. Verify reports healthy services.
2. Browser sign-in works and the supplied synthetic sample is visible.
3. Stop, start, verify, and sign in again; the same sample remains.
4. Use daily **start**, not a new install, for later sessions.

This proves the core stack, not inference or a complete grading demonstration.

## 4. Rehearse one complete run

Use the kit's compatible synthetic sample/rubric with your host. Confirm the
model/provider, run one item, inspect evidence and rationale, save a human
review, export, and reopen the export. Record what passed and the package/model.

For a fully local claim, also verify that the intended local model is downloaded,
loaded, reachable by the stack, and successfully used for the task. Record the
processing route and network dependencies. Public images include neither model
weights nor a verified offline configuration.

The new public notes practice is a manual/browser exercise. Its OASIS import
and end-to-end acceptance remain pending; its authored answers are not model
results.

[Facilitator guide](facilitator-guide.md) · [Support](support.md)
