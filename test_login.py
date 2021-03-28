import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

import json

# set wait time between testcases
waitTime = 1

# file to retrieve registered accounts
filename = "registeredAccounts.json"

# NEED TO EDIT THIS BASED ON WHERE YOUR CHROMEDRIVER IS
PATH = "C:\\chromedriver.exe"

driver = webdriver.Chrome(PATH)


def test_register(keys_username, keys_password):
    driver.get("http://127.0.0.1:8000/logout/")

    try:
        # username
        input_username = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "username"))
        )
        input_username.clear()
        input_username.send_keys(keys_username)

        # password
        input_password = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "password"))
        )
        input_password.clear()
        input_password.send_keys(keys_password)

        # press enter
        input_password.send_keys(Keys.RETURN)

        # print statements
        print("keys_username: " + keys_username)
        print("keys_password: " + keys_password)

        if (driver.title == "SingHealth WebApp"):
            isValid = True
            print("TESTCASE: VALID! LOGGED IN	✓")
        else:
            isValid = False
            print("TESTCASE: FAILED, CANNOT LOG IN")
        print()

        time.sleep(waitTime)
    except:
        print("TEST FAILED TO RUN")
        time.sleep(5)
        driver.quit()


# Opening JSON file
f = open(filename)

# returns JSON object as
# a dictionary
data = json.load(f)

# Iterating through the json
# list
for i in data['accounts']:
    username = i['username']
    password = i['password']
    test_register(username, password)

# Closing file
f.close()
