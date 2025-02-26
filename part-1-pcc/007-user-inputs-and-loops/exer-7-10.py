"""
7-10. Dream Vacation: Write a program that polls users about their dream
vacation. Write a prompt similar to If you could visit one place in the world,
where would you go? Include a block of code that prints the results of the poll.
"""

responses = {}


question = 'If you could visit one place in the world, where would you go? '
cont = 'yes'
while cont == 'yes':
    name = input('What is your name? ')
    place = input(question)
    responses[name] = place
    cont = input('Would you like to ask another person? (yes/no): ')

print()
print('---RESULTS---')
for name, place in responses.items():
    print(f'{name.title()} would like to go to: {place.title()}')
print('-------------')
