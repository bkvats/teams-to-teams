import sys
import shutil
from pathlib import Path

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from driver import get_driver
from config import url, close_window
from exceptions import SignInException

def exit_program():
    close_window()
    print("**** Thanks for using my code ****")
    sys.exit(0)
    return


def open_page(sign_in = False):
    get_driver().get(url)
    if sign_in:
        return
    profile_button_status = WebDriverWait(get_driver(), 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-tid="me-control-avatar-presence"]')))
    if profile_button_status.get_attribute("aria-label") == "unknown":
        raise SignInException("Not on the main page interface...")
    return

def clear_cache():
    shutil.rmtree(str(Path.home() / "ChromeDebug"))
    return