from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel
from PyQt5.QtCore import QTimer
from utils import clean_ram, clean_storage, get_system_info, check_for_updates, install_updates, run_windows_defender_scan

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("PC Manager")
        self.setGeometry(100, 100, 400, 400)

        # Create layout
        layout = QVBoxLayout()

        # Create buttons for cleaning RAM, cleaning storage, checking updates, and antivirus scan
        self.clean_ram_btn = QPushButton("Optimize RAM")
        self.clean_storage_btn = QPushButton("Clean Storage")
        self.check_updates_btn = QPushButton("Check for Updates")
        self.install_updates_btn = QPushButton("Install Updates")
        self.run_antivirus_btn = QPushButton("Run Antivirus Scan")
        self.status_label = QLabel("Status: Idle")  # Label to show status of actions

        # Add buttons and label to layout
        layout.addWidget(self.status_label)
        layout.addWidget(self.clean_ram_btn)
        layout.addWidget(self.clean_storage_btn)
        layout.addWidget(self.check_updates_btn)
        layout.addWidget(self.install_updates_btn)
        layout.addWidget(self.run_antivirus_btn)

        # Connect buttons to their respective functions
        self.clean_ram_btn.clicked.connect(self.handle_clean_ram)
        self.clean_storage_btn.clicked.connect(self.handle_clean_storage)
        self.check_updates_btn.clicked.connect(self.handle_check_for_updates)
        self.install_updates_btn.clicked.connect(self.handle_install_updates)
        self.run_antivirus_btn.clicked.connect(self.handle_run_antivirus)

        # Create a timer for system monitoring (CPU, RAM, Disk usage)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_system_info)
        self.timer.start(2000)  # Update every 2 seconds

        # Label for system information
        self.system_info_label = QLabel("CPU: 0%, RAM: 0%, Disk: 0%")
        layout.addWidget(self.system_info_label)

        self.setLayout(layout)

    def handle_clean_ram(self):
        """Handle the action for cleaning RAM."""
        self.status_label.setText("Status: Optimizing RAM...")
        clean_ram()  # Call the clean_ram function from utils.py
        self.status_label.setText("Status: RAM Optimized!")

    def handle_clean_storage(self):
        """Handle the action for cleaning storage."""
        self.status_label.setText("Status: Cleaning Storage...")
        clean_storage()
        self.status_label.setText("Status: Storage Cleaned!")

    def handle_check_for_updates(self):
        """Handle the action for checking system updates."""
        self.status_label.setText("Status: Checking for updates...")
        check_for_updates()
        self.status_label.setText("Status: Updates Checked!")

    def handle_install_updates(self):
        """Handle the action for installing updates."""
        self.status_label.setText("Status: Installing updates...")
        install_updates()
        self.status_label.setText("Status: Updates Installed!")

    def handle_run_antivirus(self):
        """Handle the action for running antivirus scan."""
        self.status_label.setText("Status: Running Antivirus Scan...")
        run_windows_defender_scan()
        self.status_label.setText("Status: Antivirus Scan Complete!")

    def update_system_info(self):
        """Update system information (CPU, RAM, Disk)."""
        system_info = get_system_info()
        self.system_info_label.setText(f"CPU: {system_info['CPU']}% | RAM: {system_info['RAM']}% | Disk: {system_info['Disk']}%")

def create_gui():
    """Create and run the GUI application."""
    app = QApplication([])  # Create an application instance
    window = MainWindow()  # Create the main window
    window.show()  # Show the window
    app.exec_()  # Start the application event loop
