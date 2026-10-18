from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import sys, time

from config import close_window, open_window
from driver import set_driver, get_driver
from utils import open_page, exit_program, clear_cache
from get_current_status import get_current_status
from change_current_status import change_current_status
from exceptions import SignInException

close_window()
open_window(show_window=False)
set_driver()
print("Starting the engine....")

for _ in range(3):
    try:
        open_page()
        close_window()
        open_window()
        set_driver()
        open_page()
        break
    except (TimeoutException, SignInException):
        close_window()
        clear_cache()
        open_window()
        set_driver()
        open_page(sign_in=True)
        input("Looks like you need to sign-in, kindly try signing again and then hit enter: ")

else:
    print("Too many unsuccesful attempts\nExiting....")
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
        print(f"-------------------\nCurrent Status: {get_current_status()}\n-------------------")
    elif (user_input == "2"):
        change_current_status()
        print_instructions()
    else:
        print("Kindly enter the correct input as per instructions")
        print_instructions()