import psutil

# הדפסת שימוש בדיסק, RAM ו-CPU
print('שימוש בדיסק:')
print(psutil.disk_usage('/'))

print('\nשימוש ב-RAM:')
print(psutil.virtual_memory())

print('\nשימוש ב-CPU:')
print(psutil.cpu_percent(interval=1))