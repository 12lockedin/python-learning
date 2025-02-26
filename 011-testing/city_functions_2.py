def city_country_2(city, country, population=''):
    """Return City, Country - population xxx"""
    if population:
        return f'{city.title()}, {country.title()} - population {population}'
    else:
        return f'{city.title()}, {country.title()}'