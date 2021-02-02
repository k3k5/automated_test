import unittest
import requests
import time
import json

class TestZippopotamRestAPI(unittest.TestCase):

    def setUp(self):
        self.url = 'http://api.zippopotam.us/_country_/_postal-code_'        

    def test_rest_api_for_stuttgart(self):
        self.url = self.url.replace('_country_', 'de')
        self.url = self.url.replace('_postal-code_', 'bw/stuttgart')
        response = requests.get(self.url)
        response_text = json.loads(response.text)

        # Checking for header and meta information
        self.assertEqual(200, response.status_code)

        # Checking for correct content
        self.assertEqual(response_text.get('country'), "Germany")
        self.assertEqual(response_text.get('state'), "Baden-Württemberg")
        information_for_post_code_70597 = self.find_data_for_post_code('70597', response_text.get('places'))
        self.assertIsNotNone(information_for_post_code_70597)
        self.assertEqual(information_for_post_code_70597.get('place name'), 'Stuttgart Degerloch')

    def test_rest_api_for_input_data(self):
        test_data = [
            {'country': 'us', 'postal_code': '90210', 'place_name': 'Beverly Hills'},
            {'country': 'us', 'postal_code': '12345', 'place_name': 'Schenectady'},
            {'country': 'ca', 'postal_code': 'B2R', 'place_name': 'Waverley'},
        ]
        for test in test_data:
            self.url = self.url.replace('_country_', test.get('country'))
            self.url = self.url.replace('_postal-code_', test.get('postal_code'))

            response = requests.get(self.url)
            response_text = json.loads(response.text)
            
            # Checking for header and meta information
            self.assertEqual(response.status_code, 200)
            self.assertLess(response.elapsed.total_seconds(), 1)
            self.assertEqual(response.headers.get('Content-Type'), 'application/json')
            self.assertEqual(response_text.get('places')[0].get('place name'), test.get('place_name'))

            # reset url back to normal
            self.url = 'http://api.zippopotam.us/_country_/_postal-code_'   


    def find_data_for_post_code(self, post_code: str, response_text: list):
        for item in response_text:
            if item.get('post code') == post_code:
                return item
        return None

    def tearDown(self):
        pass
