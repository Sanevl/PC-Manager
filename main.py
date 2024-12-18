import logging
import os
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget
from PyQt5.QtCore import QTimer
from resource_monitor import monitor_resources, get_system_info
from cleaner import clean_ram, clean_storage
from updater import check_updates
from antivirus import scan_system
from scheduler import start_scheduler
from gui import create_gui
import psutil



# Create log folder if it doesn't exist
if not os.path.exists("logs"):
    os.makedirs("logs")

logging.basicConfig(filename="logs/pc_manager.log", level=logging.DEBUG,
                    format="%(asctime)s - %(levelname)s - %(message)s")

def main():
    create_gui()
    logging.info("PC Manager started.")
    app = QApplication(sys.argv)

    # Start Scheduler
    start_scheduler()

    # Create the GUI
    window = create_gui()
    window.show()

    # Execute the application
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()