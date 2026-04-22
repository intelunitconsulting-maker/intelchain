# intelChain — OSINT Evidence Sealing

IntelChain is a lightweight forensic-oriented tool designed to preserve digital evidence integrity using SHA256 hashing and RFC3161 trusted timestamping.

---

## Features

* SHA256 hashing (file integrity)
* RFC3161 trusted timestamping (FreeTSA)
* Structured forensic report generation
* Evidence packaging (tsq, tsr, report)
* Optional GUI (CustomTkinter)

---

## Requirements

Linux / WSL environment with:

* Python 3
* OpenSSL
* curl

---

## Usage

```bash
python3 intelchain.py <file> [url]
```

GUI:

```bash
python3 gui.py
```

---

## Output

Evidence folder generated:

* file.sha256
* request.tsq
* response.tsr
* report.txt
* report.sha256

---

## Notes

* Designed for Linux / WSL
* Windows execution not supported natively

---

## 👤 Author

IntelChain
