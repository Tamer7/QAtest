# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re


class Missing(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.katalon.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_missing(self):
        driver = self.driver
        time.sleep(5)
        driver.get("https://media.prod.mdn.mozit.cloud/attachments/2012/07/09/3698/391aef19653595a663cc601c42a67116/image_upload_preview.html?myPhoto=IMG_2592.HEIC")
        self.assertIn("media", driver.current_url)
        driver.find_element_by_xpath("//input[@value='Send']").click()
        time.sleep(5)



    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
