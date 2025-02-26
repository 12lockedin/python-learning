"""
6-7. People: Start with the program you wrote for Exercise 6-1 (page 102).
Make two new dictionaries representing different people, and store all three
dictionaries in a list called people. Loop through your list of people. As you
loop through the list, print everything you know about each person.
"""

# First, program from exercise 6-1
lola = {'first_name': 'Lola', 'last_name': 'Fumando', 'age': 25, 'city': 'Un bar'}

print(lola['first_name'])
print(lola['last_name'])
print(lola['age'])
print(lola['city'])

ennya = {'first_name': 'Ennya', 'last_name': 'Jurado', 'age': 46, 'city': 'Hellín'}
juan = {'first_name': 'Juan', 'last_name': 'Hernangomez', 'age': 13, 'city': 'Peru-city'}

people = [lola, ennya, juan]

for person in people:
    print(f'Hi {person['first_name']}',)
    print(f'\tLast name: {person['last_name']}')
    print(f'\tAge: {person['age']}')
    print(f'\tCity: {person['city']}\n')

