"""
11-1. City, Country: Write a function that accepts two parameters: a city name
and a country name. The function should return a single string of the form
City, Country, such as Santiago, Chile. Store the function in a module called
city_functions.py.
Create a file called test_cities.py that tests the function you just wrote
(remember that you need to import unittest and the function you want to test).
Write a method called test_city_country() to verify that calling your function
with values such as 'santiago' and 'chile' results in the correct string. Run
test_cities.py, and make sure test_city_country() passes.
"""

import unittest
from city_functions import city_country

class TestCityCountry(unittest.TestCase):
    """Tests for city_country"""

    def test_city_country(self):
        """Does something like 'Chimichangas, Kakota' work?"""
        formatted_city = city_country('chimichangas', 'kakota')
        self.assertEqual(formatted_city, 'Chimichangas, Kakota')

unittest.main()
