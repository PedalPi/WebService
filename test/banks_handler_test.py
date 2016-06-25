import unittest
import requests

from .test import Test


class BanksHanddlerTest(Test):
    def setUp(self):
        try:
            self.rest.get('')
        except requests.exceptions.ConnectionError:
            self.fail("Server is down")

    def test_get(self):
        r = self.rest.getBanks()
        self.assertEqual(Test.SUCCESS, r.status_code)

        banks = r.json()['banks']
        self.assertLess(0, len(banks))