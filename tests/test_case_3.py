import unittest
from faker import Faker
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

import tests.utils as utils

class TestSogetiWebsiteWorldwideDropdown(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome('drivers/chromedriver')
        self.original_country_list = [
            'belgium', 
            'finland', 
            'france', 
            'germany', 
            'ireland', 
            'luxembourg', 
            'netherlands', 
            'norway', 
            'spain', 
            'sweden', 
            'uk', 
            'usa'
        ]
        self.original_country_links = [
            'https://www.sogeti.be/',
            'https://www.sogeti.fi/',
            'https://www.fr.sogeti.com/',
            'https://www.sogeti.de/',
            'https://www.sogeti.ie/',
            'https://www.sogeti.lu/',
            'https://www.sogeti.nl/',
            'https://www.sogeti.no/',
            'https://www.sogeti.es/',
            'https://www.sogeti.se/',
            'https://www.uk.sogeti.com/',
            'https://www.us.sogeti.com/'
        ]

    def test_check_all_links(self):
        driver = self.driver
        driver.get("https://www.sogeti.com/")

        self.assertIn("Sogeti", driver.title)

        # Accept all cookies
        utils.accept_all_cookies(self.driver)

        worldwide_dropdown_link = self.driver.find_element_by_xpath('//*[@id="header"]/div[1]/div[2]/div[2]/div[2]')
        worldwide_dropdown_link.click()

        country_list = self.driver.find_element_by_class_name("country-list")
        self.assertTrue(country_list.is_displayed())

        self.check_all_links(country_list)

    def check_all_links(self, country_list: list):
        """
        Loops through all links given in country list and checks whether they are corrupt.

        :param country_list: list of <li> items that hold a link
        """
        country_items = [country_name for country_name in country_list.find_elements_by_tag_name("li")]

        # check if all links are present
        self.assertListEqual(self.original_country_list, [x.text.lower() for x in country_items])

        for index, link in enumerate(country_items):
            link.click()
            self.driver.switch_to.window(self.driver.window_handles[-1])
            self.assertEqual(self.driver.current_url, self.original_country_links[index])
            self.assertIn("Sogeti", self.driver.title)
            self.driver.close()
            self.driver.switch_to.window(self.driver.window_handles[0])

    def tearDown(self):
        self.driver.close()
