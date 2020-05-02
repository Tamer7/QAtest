# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re


class Incorrect(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome("/Users/tamerjar/Desktop/exams/chromedriver2")
        self.driver.implicitly_wait(30)
        self.verificationErrors = []
        self.accept_next_alert = True
        
        
     
    def test_incorrect(self):
        driver = self.driver
        driver.get( "https://media.prod.mdn.mozit.cloud/attachments/2012/07/09/3698/391aef19653595a663cc601c42a67116/image_upload_preview.html?myPhoto=exams.jpg")
        time.sleep(5)
        self.assertIn("media", driver.current_url)
        el = driver.find_element_by_id("uploadImage")
        time.sleep(5)
        el.send_keys("/Users/tamerjar/Desktop/exams/IMG_2592.HEIC")
        time.sleep(3)
        self.assertEqual("You must select a valid image file!", self.close_alert_and_get_its_text())
        driver.save_screenshot("/Users/tamerjar/Desktop/exams/screenshot.png")
        time.sleep(5)
        driver.find_element_by_xpath("//input[@value='Send']").click()

        

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to.alert
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True


    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
