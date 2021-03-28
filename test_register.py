import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

import json

from gen_username_valid import generate_username_valid
from gen_email_valid import generate_email_valid
from gen_password_valid import generate_password_valid
from gen_username_INvalid import *

# set wait time between testcases
waitTime = 1

# file to store registered accounts
# filename = "registeredAccounts.json"
filename = "C:\\Users\\admin\\projects\\seleniumtut\\Selenium Testing\\registeredAccounts.json"


# NEED TO EDIT THIS BASED ON WHERE YOUR CHROMEDRIVER IS
PATH = "C:\\chromedriver.exe"

driver = webdriver.Chrome(PATH)


def test_register(keys_username, keys_email, keys_password1, keys_password2):
    driver.get("http://127.0.0.1:8000/logout/")
    driver.get("http://127.0.0.1:8000/register/")

    try:
        # username
        input_username = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "username"))
        )
        input_username.clear()
        input_username.send_keys(keys_username)

        # email
        input_email = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "email"))
        )
        input_email.clear()
        input_email.send_keys(keys_email)

        # password1
        input_password1 = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "password1"))
        )
        input_password1.clear()
        input_password1.send_keys(keys_password1)

        # password2
        input_password2 = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "password2"))
        )
        input_password2.clear()
        input_password2.send_keys(keys_password2)

        # press enter
        input_password2.send_keys(Keys.RETURN)

        # print statements
        print("keys_username: " + keys_username)
        print("keys_email: " + keys_email)
        print("keys_password1: " + keys_password1)
        print("keys_password2: " + keys_password2)

        if (driver.title == "Login"):
            isValid = True
            print("TESTCASE: VALID! NEW ACCOUNT REGISTERED	✓")
            addToDictionary(keys_username, keys_email, keys_password1)
        else:
            isValid = False
            print("TESTCASE: invalid......................")
        print()

        time.sleep(waitTime)
    except:
        print("TEST FAILED TO RUN")
        time.sleep(5)
        driver.quit()


def addToDictionary(username, email, password):
    # if len(data) == 0:
    #     data
    dictionary = {
        'username': username,
        'email': email,
        'password': password,
    }
    temp.append(dictionary)


# test_register(generate_username_valid(), generate_email_valid(),
#               keys_password1, keys_password2)
# test_register(generate_username_valid(), generate_email_valid(),
#               keys_password1, keys_password2)
# test_register(generate_username_valid(), generate_email_valid(),
#               keys_password1, keys_password2)
# test_register(generate_username_valid(), generate_email_valid(),
#               keys_password1, keys_password2)
# test_register(generate_username_valid(), generate_email_valid(),
#               keys_password1, keys_password2)

# dir_path = os.path.dirname(os.path.realpath(__file__))
# print(dir_path)

password1 = generate_password_valid()
password2 = generate_password_valid()
password3 = generate_password_valid()
password4 = generate_password_valid()
password5 = generate_password_valid()
password6 = generate_password_valid()
password7 = generate_password_valid()
password8 = generate_password_valid()
password9 = generate_password_valid()


with open(filename, "r+") as file:
    data = json.load(file)
    temp = data['accounts']

# username:
# generate_username_valid()
# generate_username_INvalid_taken()
# generate_username_INvalid_chars()

# test_register(generate_username_valid(), generate_email_valid(),
#               password1, password1)
# test_register(generate_username_valid(), generate_email_valid(),
#               password2, password2)
# test_register(generate_username_valid(), generate_email_valid(),
#               password3, password3)
# test_register(generate_username_valid(), generate_email_valid(),
#               password4, password4)
# test_register(generate_username_valid(), generate_email_valid(),
#               password5, password5)
# test_register(generate_username_valid(), generate_email_valid(),
#               password6, password6)
test_register(generate_username_INvalid_taken(), generate_email_valid(),
              password7, password7)
test_register(generate_username_INvalid_taken(), generate_email_valid(),
              password8, password8)
test_register(generate_username_INvalid_taken(), generate_email_valid(),
              password9, password9)

# file.seek(0)
# json.dump(data, file)

with open(filename, 'w') as f:
    json.dump(data, f, indent=4)

# test_register(keys_username, generate_email_valid(),
#               password1, password1)
# test_register(keys_username, generate_email_valid(),
#               password2, password2)
# test_register(keys_username, generate_email_valid(),
#               password3, password3)
# test_register(keys_username, generate_email_valid(),
#               password4, password4)
# test_register(keys_username, generate_email_valid(),
#               password5, password5)
# test_register(keys_username, generate_email_valid(),
#               password6, password6)
# test_register(keys_username, generate_email_valid(),
#               password7, password7)
# test_register(keys_username, generate_email_valid(),
#               password8, password8)
# test_register(keys_username, generate_email_valid(),
#               password9, password9)


# test_register("c", "c@gmai.com", "ajfkadflkadjflkad", "ajfkadflkadjflkad")
# test_register(keys_username, keys_email, keys_password1, keys_password2)
