# Demo help

## Start with the failed step

For package access, models or installation failures, contact the host who
supplied your kit. A repository clone is not the kit. A host-only GitHub link
returning 404 may need an access check. The published public AMD64 images need
no registry login; prepared ARM64 coordinates do not yet establish availability.
Check [current platform status](runtime.md) before changing authentication.

| Symptom | Safe next step |
| --- | --- |
| No kit or unclear platform/version | Ask the supplying host for the matching complete kit, hash and prerequisites. Do not assemble an installation from image coordinates alone. |
| Hash, prerequisite or plan check fails | Stop before installation; report the exact sanitized check and package version. Preserve the downloaded file. |
| Services unhealthy, port conflict or existing root mismatch | Use the kit's status/verify instructions and report the failed service/check. Preserve the existing instance; do not reset or adopt it blindly. |
| Browser sign-in fails | Confirm the kit's own app URL and locally generated account/helper. Keep credential values private; a public issue cannot troubleshoot a password by seeing it. |
| Named sample missing | Verify the account, instance and exact sample with the host. Do not import a substitute private record or expose a broad record catalog. |
| Media absent or not playing | Confirm that the selected sample has media and the package supports that route. Try a normal page reload after an upgrade; report input type, source-label state and sanitized playback error. |
| Local model unavailable or run fails | Stop the planned live segment and use the saved-result/manual fallback. Confirm route/readiness with the host before retrying or switching to a provider. |
| Export toast appears but no file arrives | Check browser downloads and the named run, reopen the page if needed, then request the saved export again. Do not rerun grading to recover a file. |
| Downloaded export does not match | Preserve it privately and record which expected sample/criterion count or field differed. Do not attach result data to a public issue. |

## Report a public documentation or demo problem

For a broken public link, unclear instructions or a reproducible synthetic-demo
problem, [open a public issue](https://github.com/JamiesonLabUTSW/oasis-demo/issues/new).
Use this short template:

```text
Public demo or guide and step:
OS and architecture (generic):
Package version / manifest selection:
Expected behavior:
Observed behavior and sanitized error:
Reproduces with the named public synthetic example: yes / no / not tested
Checks already completed:
```

Do not attach real/de-identified notes, institutional rubrics, private media,
`.env`, keys, passwords, full diagnostic archives, host paths or `demo-access.html`.
Inspect screenshots too. Report a suspected disclosure privately to the host
without repeating the material in a public issue.

Preserve failed installations for diagnosis. Do not reset Docker, prune volumes,
delete instances, borrow credentials or disable device protections to make a
demonstration start. A failed installation or task is evidence to diagnose, not
a reason to replace saved data.

[Start here](audience-guide.md) · [Getting started](getting-started.md) ·
[Catalog](../README.md#demo-catalog)
