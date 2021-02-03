import unittest
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

import tests.utils as utils

class TestSogetiWebsiteAutomationLink(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome('drivers/chromedriver')

    def test_automation_link(self):
        """
        Moves to page "Automation" and checks if the navigation item has the selected CSS class.
        """
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

        # Check if 'Automation' is in page title (tab title)
        self.assertIn("Automation", driver.title)
        # ... and 'Automation' is present in page source.
        self.assertIn("Automation", driver.page_source)

        # finding and hovering above navigation item 'Services' by XPATH
        services_link_li_holder = self.driver.find_element_by_xpath("/html/body/div[1]/header/div[1]/nav/ul/li[3]")
        # finding the desired link 'Automation' by XPATH
        automation_link_li_holder = self.driver.find_element_by_xpath('//*[@id="header"]/div[1]/nav/ul/li[3]/div[2]/ul/li[7]')
        utils.move_to_element(self.driver, services_link_li_holder)
        # delay of 1 second that element is visible
        time.sleep(1)
        # asserting 'Services' link and 'Automation' link have CSS class 'selected'
        self.assertIn('selected', services_link_li_holder.get_attribute('class').split())
        self.assertIn('selected', automation_link_li_holder.get_attribute('class').split())

    def tearDown(self):
        self.driver.close()
