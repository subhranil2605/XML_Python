import unittest
from internship_subhranil import extracting


class TestExtracting(unittest.TestCase):
    def test_something(self):
        self.assertRaises(FileNotFoundError, extracting.extract_zip, 'dfd')  # add assertion here


if __name__ == '__main__':
    unittest.main()
