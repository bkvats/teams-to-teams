from selenium.common.exceptions import NoSuchElementException

def get_current_status(driver, By):
    try:
        driver.find_element(By.CSS_SELECTOR, '[data-tid="set-presence-status-menu-item"]')
    except NoSuchElementException:
        avatar_panel = driver.find_element(By.CSS_SELECTOR, '[data-tid="me-control-avatar-trigger"]')
        avatar_panel.click()
        current_status = get_current_status(driver, By)
        avatar_panel.click()
        return current_status
    return driver.execute_script("""return document.querySelector('[data-tid="set-presence-status-menu-item"]').firstElementChild.nextElementSibling.innerText;""")
