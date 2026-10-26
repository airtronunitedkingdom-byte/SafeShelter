# Virtual Arena (v1.0.0)

Android Work Profile manager based on [Shelter](https://github.com/PeterCxy/Shelter), licensed under GPL-3.0. This repository is an independent adaptation, not an official Shelter release.

## Installable APK
GitHub Actions builds an installable **debug-signed APK** on push. Download the Actions artifact, extract the ZIP and install the APK using Android's permitted **Install unknown apps** setting. Google Play Store is not required. Debug signing is for testing, not a trusted production release. Verify the APK and only install builds from a trusted workflow. Android Work Profile support is required on the device.

## Features inherited from Shelter
Work Profile creation, cloning/installing apps, freeze/unfreeze, shortcuts, profile isolation and other upstream capabilities. Some functionality varies by Android version and manufacturer. APK package installation permission is preserved; it does not bypass Android installer consent.

## Branding / info
Version 1.0.0 (code 1), light interface, Virtual Arena branding and an in-app About/Privacy screen source. Integration and comprehensive security review remain to be completed before production use.

## Security and privacy
This project does not aim to bypass Android security. Work Profile managers require elevated profile management access. **Do not consider the first CI artifact independently audited.** No analytics or advertising SDK is intentionally introduced here. Upstream dependencies and permissions must be reviewed before a production release.

## License
GPL-3.0 — source based on Shelter by PeterCxy. Full upstream license applies; keep original credits and license notices.
