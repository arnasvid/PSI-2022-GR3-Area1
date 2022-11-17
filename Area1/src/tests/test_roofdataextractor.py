import unittest
from unittest import TestCase
from roofdata.check_format import cf
from roofdata.xml_to_json import xtj
from roofdata.extract_roof_data import erd


class MyTest(TestCase):
    def test_successful_check_format(self):
        self.assertTrue(cf("src/XMLFiles/stogas.xml"))

    def test_failed_check_format(self):
        self.assertFalse(cf("src/XMLFiles/bad_stogas.xml"))

    def test_check_format_raises_file_not_found_error(self):
        with self.assertRaises(FileNotFoundError):
            cf("src/XMLFiles/doesnt_exist.xml")

    def test_successful_xml_to_json(self):
        self.assertTrue(xtj("src/XMLFiles/stogas.xml"))

    def test_failed_xml_to_json(self):
        self.assertFalse(xtj("src/XMLFiles/bad_stogas.xml"))

    # def test_successful_extract_roof_data(self):
    #     try:
    #         self.assertTrue(erd(xtj("src/XMLFiles/stogas.xml")))
    #     except:
    #         print("Failed to extract roof data")
    #     raise Exception("Failed to extract roof data")

    # def test_failed_extract_roof_data(self):
    #     self.assertRaises(Exception)
    #     erd(xtj("src/XMLFiles/bad_stogas.xml"))


if __name__ == '__main__':
    unittest.main()
