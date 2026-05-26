import sys
import hashlib
import os
import subprocess
from datetime import datetime
import shutil

from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

banner = """
      ██╗███╗   ██╗████████╗███████╗██╗      ██████╗██╗  ██╗ █████╗ ██╗███╗   ██╗
      ██║████╗  ██║╚══██╔══╝██╔════╝██║     ██╔════╝██║  ██║██╔══██╗██║████╗  ██║
      ██║██╔██╗ ██║   ██║   █████╗  ██║     ██║     ███████║███████║██║██╔██╗ ██║
      ██║██║╚██╗██║   ██║   ██╔══╝  ██║     ██║     ██╔══██║██╔══██║██║██║╚██╗██║
      ██║██║ ╚████║   ██║   ███████╗███████╗╚██████╗██║  ██║██║  ██║██║██║ ╚████║
      ╚═╝╚═╝  ╚═══╝   ╚═╝   ╚══════╝╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝

            ----------------- OSINT Evidence Sealing Tool -----------------
"""


def sha256(file_path):
    h = hashlib.sha256()

    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            h.update(chunk)

    return h.hexdigest()


def run_intelchain(file, url=None):

    print("\033[94m" + banner + "\033[0m")

    if not os.path.exists(file):
        raise FileNotFoundError("File not found")

    now_dt = datetime.now()
    timestamp_folder = now_dt.strftime("%Y-%m-%d_%H-%M-%S")

    case_dir = os.path.join(os.getcwd(), "Evidence", timestamp_folder)

    os.makedirs(case_dir, exist_ok=True)

    filename = os.path.basename(file)

    shutil.copy2(file, os.path.join(case_dir, filename))

    digest = sha256(file)

    print("sha256:", digest)

    with open(os.path.join(case_dir, "file.sha256"), "w") as f:
        f.write(digest)

    # CREATE TIMESTAMP REQUEST

    subprocess.run(
        f'openssl ts -query -data "{file}" -sha256 -out "{case_dir}/request.tsq"',
        shell=True,
        check=True
    )

    # TSA REQUEST

    subprocess.run(
        f'curl -H "Content-Type: application/timestamp-query" '
        f'--data-binary @"{case_dir}/request.tsq" '
        f'http://timestamp.sectigo.com > "{case_dir}/response.tsr"',
        shell=True,
        check=True
    )

    # READ TSA RESPONSE

    result = subprocess.run(
        f'openssl ts -reply -in "{case_dir}/response.tsr" -text 2>&1',
        shell=True,
        capture_output=True,
        text=True
    )

    tsa_output = result.stdout

    timestamp_date = "UNKNOWN"
    timestamp_status = "UNKNOWN"

    for line in tsa_output.splitlines():

        if "Time stamp:" in line:
            timestamp_date = line.split("Time stamp:")[-1].strip()

        if "Status:" in line:
            timestamp_status = (
                line.split("Status:")[-1]
                .strip()
                .replace(".", "")
            )

    print("\n--- IntelChain Result ---")
    print(f"File: {file}")
    print(f"SHA256: {digest}")
    print(f"TSA Status: {timestamp_status}")
    print(f"TSA Timestamp: {timestamp_date}")
    print(f"Saved in: {case_dir}")

    now = now_dt.strftime("%Y-%m-%d %H:%M:%S")

    iso_now = now_dt.replace(microsecond=0).isoformat()

    offset = now_dt.astimezone().strftime("%z")

    offset_fmt = offset[:3] + ":" + offset[3:]

    size = os.path.getsize(file)

    report_path = os.path.join(case_dir, "report.txt")

    with open(report_path, "w") as report:

        report.write("=== INTELCHAIN REPORT ===\n\n")

        report.write(f"Case ID: {timestamp_folder}\n")
        report.write(f"Date: {now}\n")
        report.write(f"ISO 8601: {iso_now}\n")
        report.write(f"UTC Offset: {offset_fmt}\n")
        report.write("Time Source: Local system clock (non-authoritative)\n")
        report.write("Authoritative Time Source: RFC3161 TSA (Sectigo)\n")
        report.write("Timezone: Local system time\n")
        report.write("Note: TSA timestamp is in UTC (GMT)\n\n")

        report.write("=== File Information ===\n\n")
        report.write(f"File Name: {filename}\n")
        report.write(f"File Size: {size} bytes\n")
        report.write("Location: Included in evidence package\n\n")

        if url:

            report.write("=== Source Evidence ===\n\n")
            report.write(f"URL: {url}\n")
            report.write("Evidence Type: Screenshot\n")
            report.write(
                "Note: Screenshot represents the visible content at the time of capture.\n\n"
            )

        report.write("=== Integrity ===\n\n")
        report.write(f"SHA256: {digest}\n")
        report.write("Hash computed prior to timestamp request.\n\n")

        report.write("=== Verification Instructions ===\n\n")
        report.write("1. Recompute SHA256 hash of the original file\n")
        report.write("2. Compare with file.sha256\n")
        report.write("3. Inspect response.tsr with OpenSSL:\n")
        report.write(
            "   openssl ts -reply -in response.tsr -text\n\n"
        )

        report.write("=== Timestamp Authority ===\n\n")
        report.write(f"TSA Status: {timestamp_status}\n")
        report.write(f"TSA Timestamp: {timestamp_date}\n")
        report.write("Authority: Sectigo TSA\n")
        report.write("Standard: RFC3161\n")
        report.write(
            "TSA Response File: response.tsr (included in evidence package)\n"
        )
        report.write(
            "TSA Request File: request.tsq (included in evidence package)\n\n"
        )

        report.write("=== Method ===\n\n")
        report.write(
            "SHA256 hashing + RFC3161 trusted timestamping\n\n"
        )

        report.write("=== Chain of Custody ===\n\n")
        report.write(
            "The original file was copied into the evidence directory without modification.\n"
        )
        report.write(
            "A SHA256 hash was computed prior to timestamp submission.\n"
        )
        report.write(
            "The hash was submitted to a trusted timestamp authority (RFC3161).\n"
        )
        report.write(
            "The timestamp response was received and stored.\n"
        )
        report.write(
            "All generated artifacts are stored within this evidence package.\n\n"
        )

        report.write("=== Evidence Package ===\n\n")

        report.write(
            "The following files are included for independent verification:\n\n"
        )

        report.write("- Original file copy\n")
        report.write("- file.sha256\n")
        report.write("- request.tsq\n")
        report.write("- response.tsr\n")
        report.write("- report.txt\n")
        report.write("- report.txt.sha256\n")
        report.write("- report.pdf\n")
        report.write("- report.pdf.sha256\n")
        report.write("- evidence archive (.zip)\n")
        report.write("- package.sha256\n\n")

        report.write("=== Statement ===\n\n")

        report.write(
            "This document constitutes a verifiable forensic record of the digital evidence processing.\n"
        )

        report.write(
            "The associated file was hashed using SHA256 prior to submission to a trusted timestamp authority (RFC3161).\n"
        )

        report.write(
            "The timestamp provides cryptographic proof that the hash of the file existed at the specified time.\n"
        )

        report.write(
            "Any alteration of the original file would result in a different hash, invalidating this record.\n\n"
        )

        report.write("=== Report Integrity ===\n\n")
        report.write(
            "SHA256 of this report stored in report.txt.sha256\n"
        )
        report.write(
            "SHA256 of PDF stored in report.pdf.sha256\n"
        )

    report_hash = sha256(report_path)

    with open(os.path.join(case_dir, "report.txt.sha256"), "w") as f:
        f.write(report_hash)

    print(f"Report SHA256: {report_hash}")
    print(f"Report generated: {report_path}")

    # PDF

    pdf_path = os.path.join(case_dir, "report.pdf")

    styles = getSampleStyleSheet()

    doc = SimpleDocTemplate(
        pdf_path,
        author="IntelChain Tool",
        title="IntelChain Report"
    )

    title_style = styles["Heading1"]
    section_style = styles["Heading2"]
    text_style = styles["Normal"]

    content = []

    with open(report_path, "r") as f:

        for line in f:

            line = line.strip()

            if line.startswith("=== INTELCHAIN REPORT"):
                content.append(Paragraph(line, title_style))

            elif line.startswith("==="):
                content.append(Paragraph(line, section_style))

            elif line == "":
                content.append(Paragraph(" ", text_style))

            else:
                content.append(Paragraph(line, text_style))

    doc.build(content)

    print(f"PDF generated: {pdf_path}")

    pdf_hash = sha256(pdf_path)

    with open(os.path.join(case_dir, "report.pdf.sha256"), "w") as f:
        f.write(pdf_hash)

    print(f"PDF SHA256: {pdf_hash}")

    # ZIP

    zip_path = shutil.make_archive(case_dir, 'zip', case_dir)

    zip_hash = sha256(zip_path)

    with open(os.path.join(case_dir, "package.sha256"), "w") as f:
        f.write(zip_hash)

    print(f"Evidence ZIP: {zip_path}")
    print(f"ZIP SHA256: {zip_hash}")

    return case_dir


if __name__ == "__main__":

    if len(sys.argv) < 2:
        print("usage: intelchain <file> [url]")
        exit()

    file = sys.argv[1]

    url = sys.argv[2] if len(sys.argv) > 2 else None

    result = run_intelchain(file, url)

    print("Saved in:", result)
