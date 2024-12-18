import psutil
import subprocess
import platform
import os


def clean_ram():
    """Optimize RAM by closing unnecessary apps and freeing memory."""
    
    # List of essential system processes (don't terminate these)
    essential_processes = [
        'explorer.exe', 'chrome.exe', 'firefox.exe', 'python.exe', 'taskmgr.exe',
        'svchost.exe', 'lsass.exe', 'csrss.exe', 'services.exe'
    ]

    # For Linux: Clear page cache, dentries, and inodes to free up memory
    if platform.system() == 'Linux':
        subprocess.run(['sync'])
        subprocess.run(['echo', '3', '>', '/proc/sys/vm/drop_caches'])
        print("Linux RAM optimization complete.")
    
    # For Windows: Terminate non-essential processes consuming too much memory
    elif platform.system() == 'Windows':
        for proc in psutil.process_iter(['pid', 'name', 'memory_info']):
            try:
                # Skip essential processes
                if proc.info['name'].lower() in essential_processes:
                    continue

                # If the process is using too much memory, terminate it
                if proc.info['memory_info'].rss > 200 * 1024 * 1024:  # If using more than 200 MB
                    print(f"Terminating high memory process: {proc.info['name']} (PID: {proc.info['pid']})")
                    proc.terminate()  # Attempt a graceful termination
                    proc.wait()  # Wait for process to terminate gracefully

            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                # Handle cases where process may disappear or cannot be accessed
                continue

        print("Windows RAM optimization complete.")


def clean_storage():
    """Clean up storage by removing temporary files."""
    if platform.system() == 'Windows':
        subprocess.run('del /q/f/s %TEMP%\\*', shell=True)  # Delete temporary files
        subprocess.run('del /q/f/s %SystemRoot%\\Temp\\*', shell=True)
    elif platform.system() == 'Linux':
        subprocess.run('rm -rf ~/.cache/*', shell=True)
    
def get_system_info():
    """Retrieve system information like CPU, RAM, Disk usage."""
    cpu_percent = psutil.cpu_percent(interval=1)
    ram_percent = psutil.virtual_memory().percent
    disk_percent = psutil.disk_usage('/').percent
    return {"CPU": cpu_percent, "RAM": ram_percent, "Disk": disk_percent}

def check_for_updates():
    """Check for updates (dummy function for demonstration)."""
    print("Checking for updates...")

def install_updates():
    """Install updates (dummy function for demonstration)."""
    print("Installing updates...")

def run_windows_defender_scan():
    """Run a Windows Defender scan (dummy function)."""
    print("Running Windows Defender scan...")
