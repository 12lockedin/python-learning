"""
11-2. Population: Modify your function so it requires a third parameter,
population. It should now return a single string of the form City, Country –
population xxx, such as Santiago, Chile – population 5000000. Run
test_cities.py again. Make sure test_city_country() fails this time.
Modify the function so the population parameter is optional. Run
test_cities.py again, and make sure test_city_country() passes again.
Write a second test called test_city_country_population() that verifies you can call your function with the values 'santiago', 'chile', and
'population=5000000'. Run test_cities.py again, and make sure this new test
passes.
"""

import unittest
from city_functions_2 import city_country_2

class TestCityCountry(unittest.TestCase):
    """Tests for city_country"""

    def test_city_country(self):
        """Does something like 'Chimichangas, Kakota' work?"""
        formatted_city = city_country_2('chimichangas', 'kakota')
        self.assertEqual(formatted_city, 'Chimichangas, Kakota')

    def test_city_country_pop(self):
        """Does something like 'Makoto, Kochama - population 3000' work?"""
        formatted_city = city_country_2('makoto', 'kochama', 3000)
        self.assertEqual(formatted_city, 'Makoto, Kochama - population 3000')

unittest.main()