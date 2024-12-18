from apscheduler.schedulers.background import BackgroundScheduler
from resource_monitor import monitor_resources
from cleaner import clean_ram, clean_storage
from updater import check_updates
from antivirus import scan_system
import logging

def start_scheduler():
    logging.info("Starting the scheduler.")
    scheduler = BackgroundScheduler()
    scheduler.add_job(monitor_resources, 'interval', minutes=5)  # Monitor every 5 minutes
    scheduler.add_job(clean_ram, 'interval', hours=1)  # Clean RAM every hour
    scheduler.add_job(clean_storage, 'interval', hours=2)  # Clean storage every 2 hours
    scheduler.add_job(check_updates, 'interval', hours=6)  # Check for updates every 6 hours
    scheduler.add_job(scan_system, 'interval', hours=12)  # Scan system every 12 hours
    scheduler.start()
    logging.info("Scheduler started.")
