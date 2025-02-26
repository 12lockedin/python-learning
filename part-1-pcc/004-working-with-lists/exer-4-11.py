#exer-4-11
"""
4-11. My Pizzas, Your Pizzas: Start with your program from Exercise 4-1
(page 60). Make a copy of the list of pizzas, and call it friend_pizzas.
Then, do the following:
•	 Add a new pizza to the original list.
•	 Add a different pizza to the list friend_pizzas.
•	 Prove that you have two separate lists. Print the message, My favorite
pizzas are:, and then use a for loop to print the first list. Print the message,
My friend’s favorite pizzas are:, and then use a for loop to print the second list. 
Make sure each new pizza is stored in the appropriate list.
"""

#exercise 4-1
# Step 1: Create a list of favorite pizzas
pizzas = ["Pepperoni", "Margherita", "Hawaiian"]

# Step 2: Use a for loop to print the name of each pizza
print("Names of my favorite pizzas:")
for pizza in pizzas:
    print(pizza)

# Step 3: Modify the loop to print a sentence about each pizza
print("\nWhy I like these pizzas:")
for pizza in pizzas:
    print(f"I like {pizza} pizza.")

# Step 4: Add a final statement about how much you like pizza
print("\nI really love pizza!")
#end ex 4-1

#friend_pizzas
friend_pizzas = pizzas[:]

pizzas.append('BBQ')
friend_pizzas.append('Carbonara')

print("My fav pizzas are:")
for pizza in pizzas:
    print(pizza)
print("My friend's fav pizzas are:" + str(friend_pizzas))
