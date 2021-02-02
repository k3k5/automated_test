import unittest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

import tests.utils as utils

class TestSogetiWebsiteAutomationLink(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome('drivers/chromedriver')

    def test_case_1(self):
        driver = self.driver
        driver.get("https://www.sogeti.com/")

        self.assertIn("Sogeti", driver.title)

        # Accept all cookies
        utils.accept_all_cookies(self.driver)

        # search for main menu item "Services"...
        services_link = self.driver.find_element_by_xpath("/html/body/div[1]/header/div[1]/nav/ul/li[3]/div/span")
        # ... and hover above it
        utils.move_to_element(self.driver, services_link)

        # Find link "Automation" by label and click on it
        automation_link = self.driver.find_element_by_link_text('Automation')
        self.assertTrue(automation_link.is_displayed())
        automation_link.click()

        self.assertIn("Automation", driver.title)
        self.assertIn("Automation", driver.page_source)

        services_link_li_holder = self.driver.find_element_by_xpath("/html/body/div[1]/header/div[1]/nav/ul/li[3]")
        automation_link_li_holder = self.driver.find_element_by_xpath("/html/body/div[1]/header/div[1]/div[5]/ul/li[7]")
        utils.move_to_element(self.driver, services_link_li_holder)
        self.assertIn('selected', services_link_li_holder.get_attribute('class').split())
        self.assertIn('selected', automation_link_li_holder.get_attribute('class').split())

    def tearDown(self):
        self.driver.close()
