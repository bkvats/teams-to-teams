import subprocess
from pathlib import Path

def open_window():
    subprocess.Popen(f'"C:/Program Files/Google/Chrome/Application/chrome.exe" --remote-debugging-port={port} --user-data-dir={str(Path.home() / "ChromeDebug")}', shell=True)
    print("Windows opened successfully")
    return

def close_window():
    subprocess.run(f'for /f "tokens=5" %a in (\'netstat -aon ^| findstr :{port}\') do taskkill /f /pid %a /t', shell=True, capture_output=True)
    print("Window closed successfully")
    return

port = 9973