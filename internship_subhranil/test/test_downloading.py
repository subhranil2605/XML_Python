import unittest
from internship_subhranil import downloading


class TestDownloading(unittest.TestCase):
    def setUp(self) -> None:
        self.url = 'http://firds.esma.europa.eu/firds/DLTINS_20210117_01of01.zip'

    def test_download_file(self):
        self.assertRaises(ValueError, downloading.download_file, 'dfsfd')


if __name__ == '__main__':
    unittest.main()
