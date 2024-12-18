import subprocess
import logging

def clean_ram():
    logging.info("Cleaning RAM...")
    subprocess.run(["cleanmgr", "/sagerun:1"], check=True)  # Windows disk cleanup

def clean_storage():
    logging.info("Cleaning storage...")
    subprocess.run(["cleanmgr", "/sagerun:1"], check=True)
