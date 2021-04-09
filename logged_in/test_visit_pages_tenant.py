import os
import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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
        input_username.send_keys("tenant1")

        # password
        input_password = driver.find_element_by_name("password")
        input_password.clear()
        input_password.send_keys("7dE6wPG3BDTumrjgk")

        # press enter
        input_password.send_keys(Keys.RETURN)

    def test_home(self):
        driver.get("http://127.0.0.1:8000/")
        self.assertEqual(driver.title, "SingHealth WebApp")

    def test_stores(self):
        driver.get("http://127.0.0.1:8000/stores/")
        self.assertEqual(driver.title, "Restricted Access")

    def test_reports(self):
        driver.get("http://127.0.0.1:8000/reports/")
        self.assertEqual(driver.title, "SingHealth WebApp - Reports")

    def test_announcements(self):
        driver.get("http://127.0.0.1:8000/announcements/")
        self.assertEqual(driver.title, "SingHealth WebApp - Announcements")

    def test_restricted(self):
        driver.get("http://127.0.0.1:8000/restricted/")
        self.assertEqual(driver.title, "Restricted Access")

    def test_send_email(self):
        driver.get("http://127.0.0.1:8000/send_email/")
        self.assertEqual(driver.title, "Restricted Access")

    # def test_statistics_page(self):
    #     driver.get("http://127.0.0.1:8000/statistics_page/")
    #     self.assertEqual(driver.title, "SingHealth WebApp")

    def test_createNonFBReport_form(self):
        driver.get("http://127.0.0.1:8000/createNonFBReport_form/")
        self.assertEqual(driver.title, "SingHealth WebApp - Create Report")

    def test_createFBReport_form(self):
        driver.get("http://127.0.0.1:8000/createFBReport_form/")
        self.assertEqual(driver.title, "SingHealth WebApp - Create Report")

    def test_createCovidReport_form(self):
        driver.get("http://127.0.0.1:8000/createCovidReport_form/")
        self.assertEqual(driver.title, "SingHealth WebApp - Create Report")

    def test_rectify_form(self):
        driver.get("http://127.0.0.1:8000/rectify_form/")
        self.assertEqual(driver.title, "SingHealth WebApp - Rectify Form")

    def test_chart(self):
        driver.get("http://127.0.0.1:8000/chart/")
        self.assertEqual(driver.title, "SingHealth WebApp - Accounts Ranking")

    def tearDown(self):
        time.sleep(waitTime)


if __name__ == '__main__':
    unittest.main()
