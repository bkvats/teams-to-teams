from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
import sys, time

from config import close_window, open_window
from driver import setup_driver, get_driver
from utils import open_page, exit_program, clear_cache
from get_current_status import get_current_status
from change_current_status import change_current_status

close_window()
open_window()
setup_driver()

for _ in range(3):
    open_page()
    try:
        # profile_button_status = WebDriverWait(get_driver(), 60).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-tid="me-control-avatar-presence"]')))
        if True or profile_button_status.get_attribute("aria-label") == "unknown":
            close_window()
            clear_cache()
            open_window()
            time.sleep(2)
            close_window()
            open_window()
            setup_driver()
            open_page()
            input("Looks like you need to sign-in, kindly try signing again and then hit enter: ")
        else:
            break
    except Exception as e:
        print(e)
        print("Not on the chatting interface page....")
        sys.exit(0)
else:
    print("Too many unsuccesful attempts\\nExiting....")
    exit_program()

def print_instructions():
    instructions = """
    Welcome to the Main Menu!
    -> Enter 0 to exit the program
    -> Enter 1 to to your current status
    -> Enter 2 to change you current status
    """
    print(instructions)

print_instructions()
user_input = True
while user_input:
    user_input = input("Enter your input: ")
    if (user_input == "" or user_input == "0"):
        exit_program()
    elif (user_input == "1"):
        print(f"-------------------\\nCurrent Status: {get_current_status()}\\n-------------------")
    elif (user_input == "2"):
        change_current_status()
        print_instructions()
    else:
        print("Kindly enter the correct input as per instructions")
        print_instructions()