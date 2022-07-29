import unittest
from city_functions import city_country

class CityTestCase(unittest.TestCase):
    """Test for city_functions.py"""
    def test_city_country(self):
        """Test the function city_country input 'hamma, syria and get Hamma, Syria,"""
        test_sampel = city_country('hamma', 'syria')
        self.assertEqual(test_sampel, "Hamma, Syria,")

    def test_city_country_population(self):
        """test the function city_country with optional arg population"""
        test_sampel = city_country('hamma', 'syria', 500000)
        self.assertEqual(test_sampel, 'Hamma, Syria - population: 500000.')

if __name__ == '__main__':
    unittest.main()
