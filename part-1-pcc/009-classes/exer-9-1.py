"""
9-1. Restaurant: Make a class called Restaurant. The __init__() method for
Restaurant should store two attributes: a restaurant_name and a cuisine_type.
Make a method called describe_restaurant() that prints these two pieces of
information, and a method called open_restaurant() that prints a message 
indicating that the restaurant is open.
Make an instance called restaurant from your class. Print the two attributes
individually, and then call both methods.
"""

class Restaurant():
    """Store some attributes of a Restaurant"""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize name and type"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    
    def describe_restaurant(self):
        """Describing the restaurant"""
        print(f'The restaurant: {self.restaurant_name.title()}, '
              f'is a {self.cuisine_type} one.')
        
    def open_restaurant(self):
        """Opening the restaurant"""
        print(f'The {self.restaurant_name.title()} is now open!!!')

restaurant = Restaurant('the calamardo', 'sushi')

print(f'The restaurant name is: {restaurant.restaurant_name}')
print(f'The restaurant type is: {restaurant.cuisine_type}')
print()
restaurant.describe_restaurant()
restaurant.open_restaurant()