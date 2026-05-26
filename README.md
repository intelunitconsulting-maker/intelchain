# IntelChain | OSINT Evidence Sealing Tool

IntelChain is a lightweight forensic-oriented tool designed to preserve digital evidence integrity using SHA256 hashing and RFC3161 trusted timestamping.

IntelChain follows a methodology aligned with digital evidence handling practices, supporting:

- Traceability
- Integrity preservation
- Proof of existence
- Independent verification

Designed for:

- Investigators
- Analysts
- Researchers
- OSINT practitioners
- Digital evidence workflows

---

# IntelChain Interface

<p align="center">
  <img src="intelchain_gui.png" alt="IntelChain GUI" width="700"/>
</p>

---

# Installation

Clone the repository:

```bash
git clone https://github.com/intelunitconsulting-maker/intelchain.git
cd intelchain
```

---

# Run IntelChain

## GUI Mode (recommended)

Launch graphical interface:

```bash
python3 gui.py
```

---

## CLI Mode

Run directly from terminal:

```bash
python3 intelchain.py <file>
```

Examples:

```bash
python3 intelchain.py screenshot.jpg
python3 intelchain.py report.pdf
python3 intelchain.py archive.zip
python3 intelchain.py evidence.mp4
python3 intelchain.py export.json
python3 intelchain.py database.db
python3 intelchain.py forensic_image.dd
```

Optional source URL:

```bash
python3 intelchain.py screenshot.jpg "https://example.com/source"
```

This adds the source reference to the verification report.

---

# Requirements

IntelChain is designed primarily for:

- Linux
- WSL
- Debian-based systems

---

## 1) Update system packages

```bash
sudo apt update
sudo apt upgrade -y
```

---

## 2) Install Python 3

```bash
sudo apt install -y python3
python3 --version
```

---

## 3) Install pip

```bash
sudo apt install -y python3-pip
pip3 --version
```

---

## 4) Install Tkinter (GUI requirement)

```bash
sudo apt install -y python3-tk
python3 -c "import tkinter; print('tkinter OK')"
```

---

## 5) Install OpenSSL

```bash
sudo apt install -y openssl
openssl version
```

---

## 6) Install curl

```bash
sudo apt install -y curl
curl --version
```

---

## 7) Install Python dependencies

Install CustomTkinter:

```bash
pip3 install customtkinter
python3 -c "import customtkinter; print('customtkinter OK')"
```

Install ReportLab:

```bash
pip3 install reportlab
python3 -c "import reportlab; print('reportlab OK')"
```

---

# Core Principles

- Integrity
- Trusted timestamping
- Traceability
- Independent verification
- Local-first processing
- Transparent evidence packaging

---

# Evidence Integrity Workflow

1. Original file copy
2. SHA256 hashing
3. RFC3161 timestamp request generation (`request.tsq`)
4. Trusted timestamp response retrieval (`response.tsr`)
5. Timestamp response parsing
6. TXT report generation
7. PDF report generation
8. ZIP evidence archive generation
9. Package integrity hashing (`package.sha256`)

---

# Example Output

## Evidence Package

Generated files:

```text
source_file.ext
file.sha256
request.tsq
response.tsr
report.txt
report.txt.sha256
report.pdf
report.pdf.sha256
package.sha256
```

---

# Why IntelChain

In OSINT investigations, preserving the integrity and timestamp of collected evidence is critical.

IntelChain provides a simple and reliable way to:

- Prove data integrity (SHA256)
- Establish trusted proof of existence (RFC3161)
- Generate structured verification reports
- Package all supporting verification artifacts

This ensures collected evidence remains:

- Verifiable
- Traceable
- Independently reviewable over time

---

# Features

- SHA256 hashing
- RFC3161 trusted timestamping (Sectigo TSA)
- TXT report generation
- PDF report generation
- Report hashing
- ZIP evidence packaging
- Package hashing
- GUI mode (CustomTkinter)
- CLI mode
- Optional source URL reference
- Local-first architecture

---

# Supported File Types

IntelChain supports virtually any readable local file, including:

- Images
- Documents
- PDFs
- Audio files
- Video files
- Archives
- Database files
- Disk images
- Logs / exported datasets
- Binary files
- Any readable local file

---

# Security & Privacy

IntelChain is designed with a strict focus on:

- Local processing
- Transparency
- Cryptographic integrity

---

## Local Execution

- No remote file access
- No telemetry
- No analytics
- No tracking
- No hidden monitoring

All operations are initiated explicitly by the user.

---

## File Handling

- Only the selected file is processed
- The original file is copied, never modified
- No unrelated files are accessed
- Evidence package remains local

---

## Network Usage

IntelChain performs limited and transparent network operations only to:

- Send a SHA256 digest to the Timestamp Authority

Important:

- The original file is never transmitted
- Only a non-reversible cryptographic hash is sent
- No evidence content leaves the local machine

---

## Timestamp Authority

Current TSA provider:

- Sectigo RFC3161 TSA

Future versions may include:

- Multiple TSA fallback servers
- Automatic failover
- Enhanced timestamp verification

---

## No Data Collection

IntelChain does NOT:

- collect personal data
- inspect unrelated files
- upload original evidence
- track usage
- transmit evidence content

---

# Disclaimer

IntelChain does not determine the truth or authenticity of content.

It helps preserve:

- integrity
- traceability
- proof of existence

of a digital file at a specific point in time.
