from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from config import port

def set_driver():
    global driver
    options = Options()
    options.debugger_address = f"127.0.0.1:{port}"
    driver = webdriver.Chrome(options=options)

def get_driver():
    return driver

driver = None