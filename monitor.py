import psutil
import time
from datetime import datetime

class SystemMonitor:
    def __init__(self):
        self.start_time = time.time()
        self.message_count = 0
        self.error_count = 0
        
    def get_uptime(self):
        uptime_seconds = time.time() - self.start_time
        days = int(uptime_seconds // (24 * 3600))
        hours = int((uptime_seconds % (24 * 3600)) // 3600)
        minutes = int((uptime_seconds % 3600) // 60)
        seconds = int(uptime_seconds % 60)
        return {
            'days': days,
            'hours': hours,
            'minutes': minutes,
            'seconds': seconds
        }
    
    def get_system_stats(self):
        cpu_percent = psutil.cpu_percent(interval=1)
        memory = psutil.virtual_memory()
        disk = psutil.disk_usage('/')
        
        return {
            'cpu': cpu_percent,
            'memory': {
                'total': memory.total,
                'used': memory.used,
                'percent': memory.percent
            },
            'disk': {
                'total': disk.total,
                'used': disk.used,
                'percent': disk.percent
            },
            'messages': {
                'sent': self.message_count,
                'errors': self.error_count,
                'success_rate': round((self.message_count - self.error_count) / max(self.message_count, 1) * 100, 2)
            }
        }
    
    def update_message_stats(self, message_count, error_count):
        self.message_count = message_count
        self.error_count = error_count
    
    def get_current_time(self):
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
