import unittest
from devopsfetch import list_users

class TestDevOpsFetch(unittest.TestCase):

    def test_list_users(self):
        result = list_users()
        self.assertIsNotNone(result)
        self.assertIsInstance(result, str)

if __name__ == '__main__':
    unittest.main()
