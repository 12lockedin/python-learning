"""
7-4. Pizza Toppings: Write a loop that prompts the user to enter a series of
pizza toppings until they enter a 'quit' value. As they enter each topping,
print a message saying you’ll add that topping to their pizza.
"""
toppings = []
message = 'Enter your topping or type "quit" to end the addition: '
query = ''

while query != 'quit':
    query = input(message)
    if query != 'quit':
        toppings.append(query)

print(f'Your toppings: {toppings}')
