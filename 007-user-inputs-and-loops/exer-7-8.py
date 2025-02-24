"""
7-8. Deli: Make a list called sandwich_orders and fill it with the names of 
various sandwiches. Then make an empty list called finished_sandwiches. Loop
through the list of sandwich orders and print a message for each order, such
as I made your tuna sandwich. As each sandwich is made, move it to the list
of finished sandwiches. After all the sandwiches have been made, print a
message listing each sandwich that was made.
"""

sandwich_orders = ['yorkcheese', 'baconcheese', 'chicken curry',
                   'butter & sugar', 'tomato & tuna', 'nutella']
finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f'Your {current_sandwich.title()} sandwich is made.')
    finished_sandwiches.append(current_sandwich)

print(f'All sandwiches finished: {finished_sandwiches}')    

