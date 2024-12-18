import subprocess
import logging

def check_updates():
    logging.info("Checking for updates...")
    try:
        result = subprocess.run(
            ["powershell", "-Command", "Get-WindowsUpdate"],
            capture_output=True,
            text=True,
            check=True
        )
        logging.info(f"Update Check Result: {result.stdout}")
    except subprocess.CalledProcessError as e:
        logging.error(f"Failed to check updates: {e}")
