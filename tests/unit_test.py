import os
import unittest
import requests
from client import MlnnClient


class MlnnClientUnitTest(unittest.TestCase):
    def setUp(self):
        self.client = MlnnClient()

    def test_langdet_api(self):
        text = 'Millennium'
        response = self.client.langdet(text)
        self.assertIn('lang', response)
        self.assertIn('source_text', response)
        self.assertEqual(response['source_text'], text)
        self.assertEqual(response['lang'], 'en')


if __name__ == '__main__':
    unittest.main()