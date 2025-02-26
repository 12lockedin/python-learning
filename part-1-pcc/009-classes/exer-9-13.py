"""
9-13. OrderedDict Rewrite: Start with Exercise 6-4 (page 108), where you
used a standard dictionary to represent a glossary. Rewrite the program using
the OrderedDict class and make sure the order of the output matches the order
in which key-value pairs were added to the dictionary.
"""

from collections import OrderedDict

# Create a dictionary of rivers and countries
rivers = OrderedDict()
rivers['nile'] = 'egypt'
rivers['amazon'] = 'brazil'
rivers['yangtze'] = 'china'

# Loop to print a sentence about each river
print("Information about rivers:")
for river, country in rivers.items():
    print(f"The {river.title()} runs through {country.title()}.")

# Loop to print the name of each river
print("\nRivers included in the dictionary:")
for river in rivers.keys():
    print(f"- {river.title()}")

# Loop to print the name of each country
print("\nCountries included in the dictionary:")
for country in rivers.values():
    print(f"- {country.title()}")