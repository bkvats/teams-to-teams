import sys
from driver import get_driver
import shutil
from pathlib import Path

def exit_program():
    print("**** Thanks for using my code ****")
    sys.exit(0)
    return


def open_page():
    print("trying to open page...")
    get_driver().get("https://teams.microsoft.com/v2/")
    return

def clear_cache():
    shutil.rmtree(str(Path.home() / "ChromeDebug"))
    print("Cached clear succesfully")
    return