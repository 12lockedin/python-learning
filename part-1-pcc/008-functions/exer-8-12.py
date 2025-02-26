"""
8-12. Sandwiches: Write a function that accepts a list of items a person wants
on a sandwich. The function should have one parameter that collects as many
items as the function call provides, and it should print a summary of the 
sandwich that is being ordered. Call the function three times, using a different
number of arguments each time.
"""

def sandwich(*elements):
    """Show all the elements a person wants in a sandwich"""
    print('---The elements of your sandwich are:---')
    for element in elements:
        print(f'\t- {element.title()}')
    print('----------------------------------------')

sandwich('peperoni', 'mamma mia', 'prosciuto', 'opá')
sandwich('queso', 'trufa', 'jamón')
sandwich('albahaca', 'tomate')