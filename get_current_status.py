from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from driver import get_driver

def get_current_status():
    try:
        get_driver().find_element(By.CSS_SELECTOR, '[data-tid="me-control-menu"]')
    except NoSuchElementException:
        get_driver().execute_script("""document.querySelector("[data-tid='me-control-avatar-trigger']").click();""")
        current_status = get_current_status()
        get_driver().execute_script("""document.querySelector("[data-tid='me-control-avatar-trigger']").click();""")
        return current_status
    return get_driver().execute_script("""return document.querySelector('[data-tid="set-presence-status-menu-item"]').firstElementChild.nextElementSibling.innerText;""")
