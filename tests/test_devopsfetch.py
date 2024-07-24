# tests/test_devopsfetch.py

import unittest
from devopsfetch import fetch_ports, fetch_users

class TestDevOpsFetch(unittest.TestCase):

    def test_ports(self):
        result = fetch_ports()
        self.assertIsInstance(result, list)

    def test_users(self):
        result = fetch_users()
        self.assertIsInstance(result, list)

if __name__ == '__main__':
    unittest.main()
