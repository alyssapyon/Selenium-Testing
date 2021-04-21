import os
import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from CONSTANTS import *
from selenium.webdriver.common.keys import Keys

# set wait time between testcases
waitTime = 1

# NEED TO EDIT THIS BASED ON WHERE YOUR CHROMEDRIVER IS
PATH = "C:\\chromedriver.exe"

driver = webdriver.Chrome(PATH)


class TestSum(unittest.TestCase):
    def setUp(self):
        driver.get("http://127.0.0.1:8000/logout/")
        # username
        input_username = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "username"))
        )
        input_username.clear()
        input_username.send_keys(admin_username)

        # password
        input_password = driver.find_element_by_name("password")
        input_password.clear()
        input_password.send_keys(admin_password)

        # press enter
        input_password.send_keys(Keys.RETURN)

    def test_logout(self):
        driver.get("http://127.0.0.1:8000/logout/")
        self.assertEqual(driver.title, "SingHealth WebApp - Login")

    def test_register(self):
        driver.get("http://127.0.0.1:8000/register/")
        self.assertEqual(driver.title, "SingHealth WebApp")

    def test_registeradmin(self):
        driver.get("http://127.0.0.1:8000/register/admin")
        self.assertEqual(driver.title, "SingHealth WebApp")

    def test_registertenant(self):
        driver.get("http://127.0.0.1:8000/register/tenant")
        self.assertEqual(driver.title, "SingHealth WebApp")

    def test_login(self):
        driver.get("http://127.0.0.1:8000/login/")
        self.assertEqual(driver.title, "SingHealth WebApp")

    def tearDown(self):
        time.sleep(waitTime)


if __name__ == '__main__':
    unittest.main()
