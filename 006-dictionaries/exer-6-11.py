"""
6-11. Cities: Make a dictionary called cities. Use the names of three cities as
keys in your dictionary. Create a dictionary of information about each city and
include the country that the city is in, its approximate population, and one fact
about that city. The keys for each city’s dictionary should be something like
country, population, and fact. Print the name of each city and all of the information you have stored about it.
"""

cities = {
    'barcelona': {
        'country': 'spain',
        'population': 3000000,
        'fact': ' Gaudi was from here'
        },
    'palo alto': {
        'country': 'USA',
        'population': 1000000,
        'fact': 'Apple started here' 
        },
    'athens': {
        'country': 'Greece',
        'population': 1000009,
        'fact': 'Nest of the ancient philosophers'
        }
}

for city, city_info in cities.items():
    print(f"Here's some info about {city.title()}:")
    print(f"\tIt belongs to {city_info['country']}")
    print(f"\tHas a population of: {city_info['population']} inhabitants")
    print(f"\tOne curious fact is that: {city_info['fact']}")
    print()

