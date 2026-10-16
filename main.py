from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
import sys

from utils import get_current_status

options = Options()
options.debugger_address = "127.0.0.1:9973"

driver = webdriver.Chrome(options=options)
# driver.get("https://teams.microsoft.com/v2/")

try:
    profile_button = WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.ID, "idna-me-control-avatar-trigger")))
except Exception:
    print("Not on the chatting interface page....")
    sys.exit(0)

print("Current Status:", get_current_status(driver, By))
