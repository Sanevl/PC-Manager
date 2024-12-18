import subprocess
import logging

def scan_system():
    logging.info("Starting Windows Defender scan...")
    try:
        result = subprocess.run(
            ["powershell", "-Command", "Start-MpScan -ScanType QuickScan"],
            capture_output=True,
            text=True,
            check=True
        )
        logging.info(f"Defender Scan Result: {result.stdout}")
    except subprocess.CalledProcessError as e:
        logging.error(f"Failed to scan with Defender: {e}")
