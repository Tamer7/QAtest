# -*- coding: utf-8 -*-
from Screenshot import Screenshot_Clipping
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re


class Tester(unittest.TestCase):
    def setUp(self):

        self.driver = webdriver.Chrome("/Users/tamerjar/Desktop/chromedriver2")
        self.driver.implicitly_wait(30)
        self.verificationErrors = []


    def test_er(self):
        driver = self.driver
        driver.get("https://media.prod.mdn.mozit.cloud/attachments/2012/07/09/3698/391aef19653595a663cc601c42a67116/image_upload_preview.html?myPhoto=exams.jpg")
        self.assertIn("media", driver.current_url)
        time.sleep(5)
        el = driver.find_element_by_id("uploadImage")
        driver.save_screenshot("/Users/tamerjar/Desktop/exams/file.png")
        el.send_keys("/Users/tamerjar/Desktop/exams/exams.jpg")
        driver.find_element_by_xpath("//input[@value='Send']").click()
        time.sleep(10)



    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
