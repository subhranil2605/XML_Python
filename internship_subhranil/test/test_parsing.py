import unittest
from internship_subhranil import parsing


class TestParsing(unittest.TestCase):
    def setUp(self) -> None:
        self.result_docs = parsing.read_xml(r"I:\xml_codes\internship_subhranil\xml_file.xml")
        self.docs_dltins = parsing.get_docs_by_file_type(self.result_docs, "DLTINS")
        self.download_links = parsing.get_download_links(self.docs_dltins)

    def test_read_xml(self):
        self.assertIsInstance(self.result_docs, parsing.NodeList)
        self.assertRaises(FileNotFoundError, parsing.read_xml, r"I:\unknown_dir\unknown_path\xml_file.xml")

    def test_get_docs_by_file_type(self):
        self.assertIsInstance(self.docs_dltins, list)

        result = parsing.get_docs_by_file_type(self.result_docs, "DLTIN")
        self.assertEqual(len(result), 0)

        # errors
        self.assertRaises(AttributeError, parsing.get_docs_by_file_type, ["dfd"], "DLTINS")
        self.assertRaises(AssertionError, parsing.get_docs_by_file_type, [], "DLTINS")

    def get_download_links(self):
        self.assertIsInstance(self.download_links, list)
        self.assertRaises(AssertionError, parsing.get_download_links, [])


if __name__ == '__main__':
    unittest.main()
