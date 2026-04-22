# 🔗 IntelChain — OSINT Evidence Sealing Tool

IntelChain is a lightweight forensic-oriented tool designed to preserve digital evidence integrity using SHA256 hashing and RFC3161 trusted timestamping.

Designed for investigators, analysts, and OSINT practitioners to ensure evidence integrity and verifiability.

---

## ⚡ Quick Start

```bash
python3 intelchain.py file.jpg
```

---

## 🎯 Why IntelChain

In OSINT investigations, preserving the integrity and timestamp of collected evidence is critical.

IntelChain provides a simple and reliable way to:

* Prove data integrity (SHA256)
* Establish trusted time of collection (RFC3161)
* Generate verifiable forensic reports

This ensures that collected evidence can be validated and trusted over time.

---

## 🚀 Features

* SHA256 hashing (file integrity)
* RFC3161 trusted timestamping (FreeTSA)
* Structured forensic report generation
* Evidence packaging (tsq, tsr, report)
* Optional GUI (CustomTkinter)

---

## ⚙️ Requirements

Linux / WSL environment with:

* Python 3
* OpenSSL
* curl

---

## ▶️ Usage

```bash
python3 intelchain.py <file> [url]
```

GUI:

```bash
python3 gui.py
```

---

## 📁 Output

Evidence folder generated:

* file.sha256
* request.tsq
* response.tsr
* report.txt
* report.sha256

---

## ⚠️ Notes

* Designed for Linux / WSL
* Windows execution not supported natively

---

## 👤 Author

IntelChain
