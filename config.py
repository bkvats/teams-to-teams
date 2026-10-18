import subprocess
from pathlib import Path

def open_window(show_window=True):
    # subprocess.Popen(f'"C:/Program Files/Google/Chrome/Application/chrome.exe" --remote-debugging-port={port} --user-data-dir={str(Path.home() / "ChromeDebug")}', shell=True)
    subprocess.Popen(f'"C:/Program Files/Google/Chrome/Application/chrome.exe" --remote-debugging-port={port} --user-data-dir={str(Path.home() / "ChromeDebug")} {"" if show_window else "--headless"} --no-first-run --no-default-browser-check --disable-notification', shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    return

def close_window():
    subprocess.run(f'for /f "tokens=5" %a in (\'netstat -aon ^| findstr :{port}\') do taskkill /f /pid %a /t', shell=True, capture_output=True)
    return

port = 9973
url = "https://teams.microsoft.com"