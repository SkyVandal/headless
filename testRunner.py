import sys
import time

import pyautogui

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from credentials import user, pwd

OW_CHANGE_MANAGEMENT = "https://onewebtest.service-now.com/nav_to.do?uri=sys_atf_test_suite.do?sys_id=af4b017c1bbe6c10ecad4199bc4bcb2c"
OW_CONFIGURATION_MANAGEMENT = "https://onewebtest.service-now.com/nav_to.do?uri=sys_atf_test_suite.do?sys_id=fc3a1b221b26701095a74195d34bcb12"
OW_CUSTOMER_SUPPORT_MANAGEMENT = "https://onewebtest.service-now.com/nav_to.do?uri=sys_atf_test_suite.do?sys_id=49053a8e1b017450ecad4199bc4bcb55"
OW_FOUNDATION = "https://onewebtest.service-now.com/nav_to.do?uri=sys_atf_test_suite.do?sys_id=41f7db041bccbc1047656467bc4bcb50"
OW_INCIDENT_MANAGEMENT = "https://onewebtest.service-now.com/nav_to.do?uri=sys_atf_test_suite.do?sys_id=fc4bc53c1bbe6c10ecad4199bc4bcb27"
OW_KNOWLEDGE_MANAGEMENT = "https://onewebtest.service-now.com/nav_to.do?uri=sys_atf_test_suite.do?sys_id=5786d7c01bccbc1047656467bc4bcb91"
OW_OUTAGE_MANAGEMENT = "https://onewebtest.service-now.com/nav_to.do?uri=sys_atf_test_suite.do?sys_id=6fb992501b10f010ecad4199bc4bcbf0"
OW_PROBLEM_MANAGEMENT = "https://onewebtest.service-now.com/nav_to.do?uri=sys_atf_test_suite.do?sys_id=f1f9645edb7fe450c2659709f49619f3"
OW_REQUEST_MANAGEMENT = "https://onewebtest.service-now.com/nav_to.do?uri=sys_atf_test_suite.do?sys_id=8358bc931b6f201047656467bc4bcb23"
OW_TASK_MANAGEMENT = "https://onewebtest.service-now.com/nav_to.do?uri=sys_atf_test_suite.do?sys_id=48c693c01bccbc1047656467bc4bcb3b"
OW_TELEPHONY_SOLUTION = "https://onewebtest.service-now.com/nav_to.do?uri=sys_atf_test_suite.do?sys_id=937647511b5d415090040e1ad34bcb27"

if(not sys.argv[1]):
    print("Invalid, please provide an auth argument!")
    exit()

print(user)

#options = webdriver.ChromeOptions()
#options.add_argument('--headless')
browser = webdriver.Chrome()#options=options)
browser.get('https://onewebtest.service-now.com/side_door')

time.sleep(1)

user_input = browser.find_element(By.ID, "user_name")
user_input.send_keys(user)

pwd_input = browser.find_element(By.ID, "user_password")
pwd_input.send_keys(pwd)

login_button = browser.find_element(By.ID, "sysverb_login")
login_button.click()

time.sleep(1)

auth_input = browser.find_element(By.ID, "txtResponse")
auth_input.send_keys(sys.argv[1])

auth_button = browser.find_element(By.ID, "sysverb_validate_mfa_code")
auth_button.click()

time.sleep(1)

def click_run_test():
    time.sleep(4)
    coords = pyautogui.locateOnScreen("run_suite_image.png", grayscale=True)
    print(coords)
    pyautogui.click(coords)
    #run_button = browser.find_element(By.ID,"35c238b253131200040729cac2dc34e0_bottom")
    #run_button.click()

    time.sleep(5)

    run_button = browser.find_element(By.ID, "run_button")
    run_button.click()

    print("Running test")
    time.sleep(10)

print("Select the number of test you want to run: ")
print("1 - OW Change Management")
print("2 - OW Configuration Management")
print("3 - OW Customer Support Management")
print("4 - OW Foundation")
print("5 - OW Incident Management")
print("6 - OW Knowledge Management")
print("7 - OW Outage Management")
print("8 - OW Problem Management")
print("9 - OW Request Management")
print("10 - OW Task Management")
print("11 - OW Telephony Solution")

print("Choose the test:")
test_to_run = int(input())

match test_to_run:
    case 1:
        browser.get(OW_CHANGE_MANAGEMENT)
        click_run_test()
    case 2:
        browser.get(OW_CONFIGURATION_MANAGEMENT)
        click_run_test()
    case 3:
        browser.get(OW_CUSTOMER_SUPPORT_MANAGEMENT)
        click_run_test()
    case 4:
        browser.get(OW_FOUNDATION)
        click_run_test()
    case 5:
        browser.get(OW_INCIDENT_MANAGEMENT)
        click_run_test()
    case 6:
        browser.get(OW_KNOWLEDGE_MANAGEMENT)
        click_run_test()
    case 7:
        browser.get(OW_OUTAGE_MANAGEMENT)
        click_run_test()
    case 8:
        browser.get(OW_PROBLEM_MANAGEMENT)
        click_run_test()
    case 9:
        browser.get(OW_REQUEST_MANAGEMENT)
        click_run_test()
    case 10:
        browser.get(OW_TASK_MANAGEMENT)
        click_run_test()
    case 11:
        browser.get(OW_TELEPHONY_SOLUTION)
        click_run_test()
    case _:
        print("Invalid test!")
        exit()



