"""
7-9. No Pastrami: Using the list sandwich_orders from Exercise 7-8, make sure
the sandwich 'pastrami' appears in the list at least three times. Add code
near the beginning of your program to print a message saying the deli has
run out of pastrami, and then use a while loop to remove all occurrences of
'pastrami' from sandwich_orders. Make sure no pastrami sandwiches end up
in finished_sandwiches.
"""
sandwich_orders = ['yorkcheese', 'pastrami', 'baconcheese', 'chicken curry',
                   'butter & sugar', 'pastrami', 'tomato & tuna', 'nutella',
                   'pastrami']

print(f'The Deli has run out of pastrami sandwiches.\n')

finished_sandwiches = []
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f'Your {current_sandwich.title()} sandwich is made.')
    finished_sandwiches.append(current_sandwich)

print(f'All sandwiches finished: {finished_sandwiches}')   