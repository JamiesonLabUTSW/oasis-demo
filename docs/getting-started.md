# Getting started

New to the terms? Read [Start here: choose your path](audience-guide.md) first.
Follow these steps with the host who supplies your kit. Keep that kit and its
README available for later startup and support.

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
| Windows Intel/AMD | Host-supplied d40f1955 AMD64 kit with Ubuntu/WSL2 and Docker Desktop; [public image manifest](../images.json) | Current resources, install, login, sample, retained restart |
| Apple Silicon Mac | Host-supplied 4abb0bb2 Mac kit with Docker Desktop; [prepared ARM64 manifest](../images-arm64.json) | Public copies pending; fresh-recipient install, login, sample, retained restart, and separately selected model route |
| Other Linux/Windows ARM | Ask for an explicitly supported package | No general support claim here |

The Apple Silicon manifest is **prepared, not published**. It lists the intended
exact image selection. Content review passed; public copies and anonymous
download verification are pending. Do not replace a supplied kit's profile or mix the two versions.
Publication will not create a general public Mac installer or qualify a fresh
recipient machine. [Runtime status](runtime.md).

Use your kit's resource checks. Chip names and total RAM do not establish
sufficient free memory, storage, or local-model capacity.

## 3. Install and sign in

In the terminal specified by the package README, verify the download hash,
check prerequisites, review the plan, install, and verify. Stop on failed checks.

The current assisted Windows kit provides `check`, `plan`, `install`,
`verify`, `guide`, `start`, `status`, and `stop` through `oasis.sh`.
Those commands work **inside that extracted kit**, not this repository.

The assisted Mac pilot uses `python3.11 pilot.py check`, `plan`, and `install`
inside its extracted kit, with `Start.command`, `Open OASIS.command` and
`Stop.command` for daily use. Follow that kit's exact prerequisites and supported
image route; a prepared public-image profile is not proof that its images can
yet be downloaded. Do not run these commands in the public library directory.

The Windows `guide` command creates a private local `demo-access.html` with copy
controls for the generated email and password. Open the printed file path.
Use the account generated or designated for your own installation. Keep the
helper on your own computer, outside Git and shared folders; do not upload,
screenshot, or serve it. Follow your specific package's guide/start behavior.

Confirm:

1. Verify reports healthy services.
2. Browser sign-in works and the supplied synthetic sample is visible.
3. Stop, start, verify, and sign in again; the same sample remains.
4. Use daily **start**, not a new install, for later sessions.

This proves the core stack, not inference or a complete grading demonstration.

For later sessions: start the existing instance with its kit, confirm health,
open its app/helper and sign in. When finished, use the kit's supported stop
command. Preserve its runtime data, kit and profile. Ask the host to resolve
port conflicts or a mismatched existing installation; do not reset it to proceed.

## 4. Explore saved results or agree a rehearsal

If your host provides a named saved synthetic result on the selected instance,
open it and confirm the sample, rubric and input type. Inspect the score,
evidence and rationale against that input. An existing result can be toured
without rerunning inference.

A fresh kit may contain seeded inputs but no completed run or export. In that
case, use the public manual notes practice until a bounded live task is agreed;
you do not need to generate a result just to finish reading this guide.

If a live run is explicitly part of the rehearsal, agree on the bounded sample,
model/provider, processing location and possible cost first. Run that selection,
inspect its results, and perform human review only on the designated practice
record. Export and reopen the actual file. Check the expected sample/criterion
rows, scores and review state. Record what passed and the package/model; a
completed run with Pending results has not received substantive human acceptance.

For media, use the host's tested audio/video or transcript route. Confirm that
playback and the displayed transcript refer to the intended sample. Read the
source/input label; displaying a recording does not mean grading used its video
or audio. See the [media explanation](audience-guide.md#media-and-transcript-demonstrations).

For a fully local claim, also verify that the intended local model is downloaded,
loaded, reachable by the stack, and successfully used for the task. Record the
processing route and network dependencies. Public images include neither model
weights nor a verified offline configuration.

The new public notes practice is a manual/browser exercise. Its OASIS import
and end-to-end acceptance remain pending; its authored answers are not model
results.

## When a step fails

Stop at the failed stage, preserve the installation and capture only the sanitized
step/error for your host. Do not reinstall repeatedly, reset Docker or retry a
model task just to recover an export. The [support guide](support.md) separates
package access, startup, media and download problems.

[Facilitator guide](facilitator-guide.md) · [Support](support.md) ·
[Start here](audience-guide.md)
