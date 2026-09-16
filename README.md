# OASIS Demo Container Images

Frozen Linux AMD64 container images for an assisted OASIS/MAPLES academic
research demonstration. These are not a production release, signed installer,
medical device, or independently validated assessment system.

## Images

The five images in [images.json](images.json) are available anonymously from
`ghcr.io/jamiesonlabutsw/oasis-demo/`. No registry login is required. Use the
immutable SHA-256 references in the manifest, not a floating tag. The human
readable tag is `d40f1955-amd64-r1`; the application revision is
`d40f19552eabaec60746922fe0e1c96cea7e1556`.

These copies preserve the original manifests and layers. Some embedded labels
therefore describe their original private canary build; they are provenance,
not a claim of a signed or generally qualified public release. No source build
was performed for this distribution.

This repository provides image coordinates and license notices only. The
assisted deployment package is supplied separately. Installing a full stack
also requires its matching Compose/bootstrap package and public PostgreSQL,
MinIO and Prefect images. Pulling these images alone does not install the stack.

The optional OASIS MCP image is not included. Model weights, provider/API keys,
user credentials, workshop data and learner notes are not distributed here.
The images include application code and synthetic examples; downloading them
allows inspection of that code. Git repository history is not included.

## License

Academic research use only. Commercial use and redistribution are prohibited
under the project terms. Public availability does not change the license and
does not imply an OSI-approved open-source license.

Copyright (c) 2026 The University of Texas Southwestern Medical Center.
Copyright (c) 2026 Andrew R. Jamieson PhD, Jamieson Lab, Lyda Hill Department of Bioinformatics.

See [LICENSE](LICENSE) for the complete project terms and
[THIRD_PARTY_NOTICES](THIRD_PARTY_NOTICES) for component and dependency notices.
Third-party components retain their own licenses.
