"""
9-2. Three Restaurants: Start with your class from Exercise 9-1. Create three
different instances from the class, and call describe_restaurant() for each
instance.
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

restaurant_1 = Restaurant('the chimichangas', 'mexican')
restaurant_2 = Restaurant('quantizied', 'cryptochicken')
restaurant_3 = Restaurant('pizzato', 'cocido')

restaurant_1.describe_restaurant()
restaurant_2.describe_restaurant()
restaurant_3.describe_restaurant()