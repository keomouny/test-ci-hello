import unittest
from main import *


class TestMain(unittest.TestCase):
    def test_reverse_word(self):
        self.assertEqual(reverse_word('maison'), 'nosiam')
        self.assertEqual(type(reverse_word('maison')), str)

    def test_reverse_number(self):
        self.assertEqual(reverse_number(12), '-12')
        self.assertEqual(reverse_number(-2), '+2')


if __name__ == '__main__':
    unittest.main(verbosity=2)
