import subprocess
import os
import time

result = subprocess.Popen('"C:/Program Files/Google/Chrome/Application/chrome.exe" --remote-debugging-port=9973 --user-data-dir=C:/ChromeDebug', shell=True)
# os.system('""C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe" --remote-debugging-port=9973 --user-data-dir="C:\\ChromeDebug""')
# time.sleep(3)
subprocess.run('for /f "tokens=5" %a in (\'netstat -aon ^| findstr :9973\') do taskkill /f /pid %a /t', shell=True, capture_output=True)
print("Target Chrome window closed.")
# print(result)