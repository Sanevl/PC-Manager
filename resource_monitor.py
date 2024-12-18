import psutil
import logging
import psutil
import platform

def get_system_info():
    """Retrieve basic system information."""
    system_info = {
        "OS": platform.system(),
        "OS Version": platform.version(),
        "CPU": platform.processor(),
        "CPU Cores": psutil.cpu_count(),
        "RAM": psutil.virtual_memory().total,
        "Storage": psutil.disk_usage('/').total,
    }
    return system_info

def monitor_resources():
    ram_usage = psutil.virtual_memory().percent
    storage_usage = psutil.disk_usage('/').percent
    cpu_usage = psutil.cpu_percent(interval=1)
    
    logging.info(f"CPU Usage: {cpu_usage}%")
    logging.info(f"RAM Usage: {ram_usage}%")
    logging.info(f"Storage Usage: {storage_usage}%")
    
    return cpu_usage, ram_usage, storage_usage
