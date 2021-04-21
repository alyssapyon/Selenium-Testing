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
PATH = chromeDriver_filepath

driver = webdriver.Chrome(PATH)

driver.get("http://www.insecurelabs.org/Talk")

inputfield = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.NAME, "query"))
)
inputfield.clear()
inputfield.send_keys(
    "<script>alert('...haha, you have been XSS-ed...')</script>")

inputfield.send_keys(Keys.RETURN)

try:
    alert_obj = driver.switch_to.alert
    alert_obj.accept()
    print("alert found")
except:
    print("no alert")


time.sleep(5)
