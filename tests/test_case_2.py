import unittest
from faker import Faker

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

import tests.utils as utils

class TestSogetiWebsiteContactForm(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome('drivers/chromedriver')

    def test_contact_form(self):
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

        # scroll to contact form
        contact_form = self.driver.find_element_by_xpath('//*[@id="__field_"]')
        utils.move_to_element(self.driver, contact_form)

        # filling form with fake data
        # IMPORTANT: Form is not filled completely based on the given testcase, ...
        self.fill_form()

        # so this will fail
        self.assertIn("Thank you", driver.page_source)

    def fill_form(self):
        """
        Fills the contact form with fake data.
        """
        # initialize Faker
        fake = Faker()
        first_name = fake.first_name()
        last_name = fake.last_name()
        email = fake.email()
        phone = fake.phone_number()
        message = fake.text()

        # Fill first name field
        first_name_field = self.driver.find_element_by_xpath('//*[@id="4ff2ed4d-4861-4914-86eb-87dfa65876d8"]')
        first_name_field.send_keys(first_name)

        last_name_field = self.driver.find_element_by_xpath('//*[@id="11ce8b49-5298-491a-aebe-d0900d6f49a7"]')
        last_name_field.send_keys(last_name)

        email_field = self.driver.find_element_by_xpath('//*[@id="056d8435-4d06-44f3-896a-d7b0bf4d37b2"]')
        email_field.send_keys(email)

        phone_field = self.driver.find_element_by_xpath('//*[@id="755aa064-7be2-432b-b8a2-805b5f4f9384"]')
        phone_field.send_keys(phone)

        message_field = self.driver.find_element_by_xpath('//*[@id="88459d00-b812-459a-99e4-5dc6eff2aa19"]')
        message_field.send_keys(message)

        accept_privacy_policy_checkbox = self.driver.find_element_by_xpath('//*[@id="863a18ee-d748-4591-bb64-ef6eae65910e"]/fieldset/label/input')
        accept_privacy_policy_checkbox.click()

        form_submit_button = self.driver.find_element_by_xpath('//*[@id="06838eea-8980-4305-83d0-42236fb4d528"]')
        form_submit_button.click()

    def tearDown(self):
        self.driver.close()