"""
6-8. Pets: Make several dictionaries, where the name of each dictionary is the
name of a pet. In each dictionary, include the kind of animal and the owner’s
name. Store these dictionaries in a list called pets. Next, loop through your list
and as you do print everything you know about each pet.
"""

rufus = {'kind': 'dog', 'owner': 'mariah'}
perez = {'kind': 'sloth', 'owner': 'flaminda'}
carlos = {'kind': 'pork', 'owner': 'camilo'}

pets = [rufus, perez, carlos]

for pet in pets:
    # The following line is completely unnecesary for this exercise, but I do it
    print(f'Name: {[k for k,v in globals().items() if v == pet][0].title()}')
    print(f'Kind: {pet['kind'].title()}')
    print(f'Owner: {pet['owner'].title()}')
    print()

