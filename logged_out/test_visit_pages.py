import os
import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# set wait time between testcases
waitTime = 1

# NEED TO EDIT THIS BASED ON WHERE YOUR CHROMEDRIVER IS
PATH = "C:\\chromedriver.exe"

driver = webdriver.Chrome(PATH)


class TestSum(unittest.TestCase):
    def setUp(self):
        driver.get("http://127.0.0.1:8000/logout/")

    def test_logout(self):
        driver.get("http://127.0.0.1:8000/logout/")
        self.assertEqual(driver.title, "SingHealth WebApp - Login")

    def test_register(self):
        driver.get("http://127.0.0.1:8000/register/")
        self.assertEqual(driver.title, "SingHealth WebApp - Register")

    def test_registeradmin(self):
        driver.get("http://127.0.0.1:8000/register/admin")
        self.assertEqual(driver.title, "SingHealth WebApp - Register Admin")

    def test_registertenant(self):
        driver.get("http://127.0.0.1:8000/register/tenant")
        self.assertEqual(driver.title, "SingHealth WebApp - Register Tenant")

    def test_login(self):
        driver.get("http://127.0.0.1:8000/login/")
        self.assertEqual(driver.title, "SingHealth WebApp - Login")

    def tearDown(self):
        time.sleep(waitTime)


if __name__ == '__main__':
    unittest.main()
