"""
9-4. Number Served: Start with your program from Exercise 9-1 (page 166).
Add an attribute called number_served with a default value of 0. Create an
instance called restaurant from this class. Print the number of customers the
restaurant has served, and then change this value and print it again.
Add a method called set_number_served() that lets you set the number
of customers that have been served. Call this method with a new number and
print the value again.
Add a method called increment_number_served() that lets you increment
the number of customers who’ve been served. Call this method with any number 
you like that could represent how many customers were served in, say, a
day of business
"""

class Restaurant():
    """Store some attributes of a Restaurant"""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize name and type"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    
    def describe_restaurant(self):
        """Describing the restaurant"""
        print(f'The restaurant: {self.restaurant_name.title()}, '
              f'is a {self.cuisine_type} one.')
        
    def open_restaurant(self):
        """Opening the restaurant"""
        print(f'The {self.restaurant_name.title()} is now open!!!')

    def set_number_served(self, num_serves):
        """Change the number of serves"""
        self.number_served = num_serves

    def increment_num_served(self, increment):
        """Increment the number of serves, reject decrease"""
        if increment >= 0:
            self.number_served += increment
        else:
            print('You cannot decrease the number of serves!!!')

restaurant = Restaurant('the calamardo', 'sushi')

print(f'The restaurant name is: {restaurant.restaurant_name}')
print(f'The restaurant type is: {restaurant.cuisine_type}')
print()
restaurant.describe_restaurant()
restaurant.open_restaurant()
print('-----------------')

print(f'Number of serves: {restaurant.number_served}') # Print intial serves
restaurant.number_served = 5 # Change number of serves
print(f'New number of serves: {restaurant.number_served}')
print(f'---using new method---')
restaurant.set_number_served(7)
print(f'New num of serves: {restaurant.number_served}')
print('---using increment method---')
restaurant.increment_num_served(int(input('Provide total serves today increase:')))
print(f'New num of serves: {restaurant.number_served}')
