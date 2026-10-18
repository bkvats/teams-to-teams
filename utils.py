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
    element = WebDriverWait(get_driver(), 15).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#loginHeader, [data-tid="me-control-avatar-presence"]')))
    if (element.get_attribute("id") == "loginHeader" and get_driver().title == "Sign in to your account") or (element.get_attribute("aria-label") == "unknown"):
        raise SignInException("User is not signed-in properly....")
    return

def clear_cache():
    shutil.rmtree(str(Path.home() / "ChromeDebug"))
    return