import unittest
from internship_subhranil import create_csv_from_xml


class TestConverting(unittest.TestCase):
    def test_get_tag_name(self):
        a = "dfs{df} hello.zip"
        self.assertEqual(create_csv_from_xml.get_tag_name(a), ' hello.zip')
        self.assertEqual(create_csv_from_xml.get_tag_name('hello.zip'), 'hello.zip')


if __name__ == '__main__':
    unittest.main()
