import unittest
from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):
    """Test for 'name_function.py"""
    def test_first_last_name(self):
        """Do names like 'Fadi Abji' work?"""
        formatted_name = get_formatted_name('fadi','abji')
        self.assertEqual(formatted_name, 'Fadi Abji')

    def test_first_last_middle_name(self):
        """Do names like 'Fadi Ghassan Abji' work?"""
        formatted_name = get_formatted_name('fadi','abji','ghassan')
        self.assertEqual(formatted_name, 'Fadi Ghassan Abji')

if __name__ == '__main__':
    unittest.main()


