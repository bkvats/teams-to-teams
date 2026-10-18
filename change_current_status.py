from utils import exit_program
from get_current_status import get_current_status
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from driver import get_driver

status_data = [[], ["Available", "me_control_presence_availability_available"], ["Busy", "me_control_presence_availability_busy"], ["Do not disturb", "me_control_presence_availability_do_not_disturb"], ["Be right back", "me_control_presence_availability_be_right_back"], ["Away", "me_control_presence_availability_appear_away"], ["Offline", "me_control_presence_availability_appear_offline"]]


def print_instructions():
    current_status = get_current_status()
    instructions = f"""
    CURRENT STATUS: {current_status}

    Choose one of the following options to change you current status
    """
    print(instructions)

    for i in range(1, len(status_data)):
        if (status_data[i][0] == current_status):
            continue
        print(f"-> Enter {i} for {status_data[i][0]}")


def change_current_status():
    print_instructions()
    user_input = True
    while user_input:
        user_input = input("\nEnter your input: ")
        if (user_input == "0"):
            return
        elif (user_input == ""):
            exit_program
        elif user_input in {str(x) for x in range(1, len(status_data) + 1)}:
            new_status = status_data[int(user_input)]
            get_driver().execute_script("""document.querySelector("[data-tid='me-control-avatar-trigger']").click();""")
            try:
                get_driver().find_element(By.CSS_SELECTOR, '[data-tid="me-control-menu"]')
            except NoSuchElementException:
                get_driver().execute_script("""document.querySelector("[data-tid='me-control-avatar-trigger']").click();""")
            get_driver().find_element(By.CSS_SELECTOR, '[data-tid="set-presence-status-menu-item"]').click()
            get_driver().find_element(By.CSS_SELECTOR, f'[data-tid="{new_status[1]}"]').click()
            get_driver().execute_script("""document.querySelector("[data-tid='me-control-avatar-trigger']").click();""")
            print(f"Status changed succesfully\nCURRENT STATUS: {get_current_status()}\n")
        else:
            print("Kindly enter the correct input as per instructions")
            print_instructions()
