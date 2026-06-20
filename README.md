<div align="center">

# IntelChain Community v1.1

### Forensic Evidence Preservation Platform

**SHA-256 Integrity Verification • RFC 3161 Trusted Timestamping • Local-First Evidence Preservation**

![Platform](https://img.shields.io/badge/platform-Windows%2010%20%2F%2011-0b1220?style=flat-square)
![Edition](https://img.shields.io/badge/edition-Community-2f6fed?style=flat-square)
![RFC3161](https://img.shields.io/badge/timestamping-RFC%203161-caa14b?style=flat-square)
![SHA256](https://img.shields.io/badge/hash-SHA--256-caa14b?style=flat-square)
![Local First](https://img.shields.io/badge/architecture-local--first-1f9d55?style=flat-square)
![No Telemetry](https://img.shields.io/badge/telemetry-none-1f9d55?style=flat-square)
![OpenSSL](https://img.shields.io/badge/crypto-OpenSSL-grey?style=flat-square)
![License](https://img.shields.io/badge/license-Community%20EULA-grey?style=flat-square)

[Website](https://intelunitconsulting.com/intelchain/) • [User Guide (PDF)](#documentation) • [Download](#download) • [License](#license)

</div>

---

# Official Website

https://intelunitconsulting.com/intelchain/

---

# Overview

IntelChain Community is a forensic-oriented evidence preservation platform designed to help maintain the integrity, traceability, and proof of existence of digital evidence through standardized cryptographic mechanisms.

The platform combines **SHA-256 integrity verification** with **RFC 3161 trusted timestamping** to establish independently verifiable evidence records while ensuring that evidence remains under the user's control at all times.

IntelChain Community is intended for:

* OSINT investigations
* Digital evidence preservation
* Research documentation
* Incident response workflows
* Independent verification processes

IntelChain follows a strict **local-first architecture**:

* No telemetry
* No analytics
* No cloud upload
* No hidden monitoring
* No remote evidence storage

> **Important.** IntelChain strengthens the technical credibility of a piece of evidence (cryptographic hash, third-party timestamp), but it does not determine its legal admissibility and does not replace an official report from a judicial officer (bailiff) for high-stakes matters. See [Documentation](#documentation) below for details.

---

# Features

* SHA-256 evidence hashing
* RFC 3161 trusted timestamping
* Timestamp token verification
* Professional PDF forensic reports
* Evidence manifest generation
* Integrity chain documentation
* ZIP evidence packaging
* Package integrity hashing
* Source URL integration
* **Browser extension (Chrome & Firefox)** — capture any web page directly from the browser
* **Full-page capture** with automatic scrolling
* Local server (`127.0.0.1:8765`) for extension ↔ application communication
* First-launch extension installation wizard
* Local evidence preservation
* Community Edition interface

---

# Documentation

A complete user guide is included with every release and available in French and English:

* `Guide_Utilisateur_IntelChain.pdf` (FR)
* `Guide_Utilisateur_IntelChain_EN.pdf` (EN)

The guide explains, in plain language:

* What problem IntelChain actually solves (the limitations of a raw screenshot)
* What each mechanism (SHA-256, RFC 3161, integrity chain) does and does not prove
* What IntelChain does **not** replace (an authentic legal act / bailiff's report)
* When to use it (disputes, OSINT, IP infringement, identity theft, journalism, etc.)
* How to independently verify a sealed package
* A full FAQ

**Read the guide before relying on IntelChain in a personal, professional, or legal context.**

---

# Screenshots

<div align="center">

| Application | Browser Extension |
|---|---|
| <img src="docs/screenshots/intelchain-gui.png" width="380" alt="IntelChain Community interface"> | <img src="docs/screenshots/intelchain-extension.png" width="380" alt="IntelChain Capture browser extension"> |
| **Generated Evidence Package** | **Verification** |
| <img src="docs/screenshots/intelchain-package.png" width="380" alt="Generated evidence package contents"> | <img src="docs/screenshots/intelchain-verify.png" width="380" alt="Forensic verification result"> |

</div>

> Screenshots are illustrative. The application interface and generated package structure may evolve between releases.

---

# Community Edition

IntelChain Community provides a lightweight environment for evidence preservation workflows while maintaining complete local control over processed evidence.

Current version:

```text
IntelChain Community v1.1
```

Compatibility:

* Windows 10 (64-bit)
* Windows 11 (64-bit)

---

# Prerequisites

* Windows 10/11 (64-bit)
* No external installation required — OpenSSL and curl are bundled with the installer

See [Troubleshooting](#troubleshooting) below if timestamp-related functions do not work as expected.

---

# Core Principles

IntelChain is designed around the following principles:

* Integrity preservation
* Proof of existence
* Independent verification
* Transparent evidence packaging
* Forensic traceability
* Local-first processing
* User control over evidence

---

# Evidence Workflow

IntelChain automatically performs the following operations:

1. Evidence import (local file or browser capture via the extension)
2. SHA-256 hash calculation
3. RFC 3161 timestamp request generation
4. Submission of the digest to the Timestamp Authority
5. Trusted timestamp retrieval
6. Timestamp verification
7. Evidence manifest creation
8. PDF forensic report generation
9. ZIP evidence archive generation
10. Final package integrity sealing (chain fingerprint)

---

# Generated Artifacts

IntelChain may generate the following directories and artifacts:

```text
evidence/
timestamp/
reports/
manifest/
integrity/
source/
```

Generated records may include:

* SHA-256 digests
* RFC 3161 timestamp request files
* RFC 3161 timestamp response tokens
* Verification reports
* Evidence manifests
* Integrity chain / sealing records
* Integrity reports (chain fingerprint)
* Sealed evidence archives

---

# Security & Privacy

IntelChain is designed with operational transparency and evidence confidentiality in mind.

## Local Processing

* Evidence files remain on the local system
* No evidence is uploaded
* No remote file storage is used
* No hidden synchronization occurs
* No telemetry data is collected

## Network Usage

Network communication occurs only during RFC 3161 timestamp operations.

IntelChain transmits:

* A SHA-256 cryptographic digest of the evidence

IntelChain does **not** transmit:

* Original evidence files
* Evidence content
* Evidence archives
* Generated reports
* Investigation data

The transmitted digest is computationally non-reversible and cannot be used to reconstruct the original evidence.

---

# Timestamp Authority

Current default provider:

* Sectigo RFC 3161 Timestamp Authority

The selected Timestamp Authority provides trusted third-party proof that a specific cryptographic digest existed at a particular point in time. It does not, by itself, validate the content of the underlying file (see [Disclaimer](#disclaimer)).

---

# Supported Evidence Types

IntelChain supports virtually any readable local file, including:

* Images
* PDFs
* Documents
* Archives
* Databases
* Log files
* Videos
* Audio files
* Disk images
* Exported datasets
* Binary files
* Web pages (via the browser extension)

---

# Standards

IntelChain relies on established cryptographic standards and practices, including:

* SHA-256 (FIPS 180-4)
* RFC 3161 Trusted Timestamping
* X.509 certificate validation

---

# Verification

Evidence packages generated by IntelChain are intended to support independent verification.

Third parties may verify:

* SHA-256 integrity values
* Timestamp token validity
* Timestamp authenticity
* Evidence package consistency
* Integrity chain / sealing documentation

using publicly available cryptographic tools (e.g. OpenSSL) and RFC 3161-compatible verification methods, without depending on IntelChain itself.

---

# Why IntelChain

Digital evidence should remain:

* Verifiable
* Traceable
* Independently reviewable
* Resistant to accidental alteration
* Preserved over time

IntelChain helps establish:

* Integrity preservation
* Trusted proof of existence
* Timestamp authenticity
* Documentation consistency
* Forensic traceability

through standardized cryptographic workflows designed for long-term verification — while remaining transparent about what it does **not** do (see [Disclaimer](#disclaimer)).

---

# Download

Official downloads are available from the Intel Unit Consulting website.

https://intelunitconsulting.com/intelchain/

The Intel Unit Consulting website is the official distribution channel for IntelChain Community releases.

Latest release:

```text
IntelChain Community v1.1
```

The release package includes the installer, the browser extension, the user guide (FR/EN), and supporting documentation (README, CHANGELOG, LICENSE).

---

# Troubleshooting

**RFC 3161 / OpenSSL issues.** IntelChain bundles the OpenSSL components required for timestamping (digest processing, timestamp request generation, response verification). In certain Windows environments, OpenSSL execution may be affected by local system configuration, security policies, or permission restrictions.

If timestamp-related functions do not operate correctly, check that OpenSSL is available and functioning by running, from the installation directory:

```text
bin\openssl.exe version
```

If version information is returned, the OpenSSL prerequisite is available and operational.

---

# License

IntelChain Community is distributed under the terms of the accompanying license agreement.

Use of IntelChain Community constitutes acceptance of the conditions set forth in that agreement.

See the `LICENSE.txt` file included with the software and repository for complete licensing information (bilingual FR/EN).

---

# Disclaimer

IntelChain does not determine the authenticity, accuracy, legality, or truthfulness of the content being preserved.

The platform provides mechanisms intended to preserve:

* Integrity
* Proof of existence
* Traceability

of a digital file at a specific point in time.

The existence of a trusted timestamp does not validate the underlying content itself, and **does not guarantee that a resulting evidence package will be accepted as admissible in any given legal proceeding.** For high-stakes or contested matters, an official report from a sworn judicial officer remains the recommended approach, in addition to sealing evidence with IntelChain as an immediate first step.

Users remain responsible for complying with applicable laws, investigative standards, and evidentiary requirements applicable within their jurisdiction.

---

<div align="center">

**IntelChain Community • Intel Unit Consulting**

[intelunitconsulting.com/intelchain](https://intelunitconsulting.com/intelchain/) • https://intelunitconsulting.com/contact/

</div>
