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

from CONSTANTS import *

# set wait time between testcases
waitTime = 1

# file to store registered accounts
filename = registeredAccounts_filepath

# NEED TO EDIT THIS BASED ON WHERE YOUR CHROMEDRIVER IS
PATH = chromeDriver_filepath
driver = webdriver.Chrome(PATH)

# run for x cycles
x = 50

waittime = 1

driver.get("http://127.0.0.1:8000/logout/")


def monkey(x):
    for i in range(x):
        time.sleep(waittime)
        links = driver.find_elements_by_tag_name("a")
        link = random.choice(links).get_attribute('href')
        if len(link) > 0:
            try:
                print("visited: " + str(link))
                driver.get(link)
            except:
                print("ERROR! Monkey found a problem!")
                print("problem link: " + str(link) + "\n")
                return
    print("monkey has finished running \n")


monkey(x)
