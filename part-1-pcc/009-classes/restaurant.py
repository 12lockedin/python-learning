"""Define the Restaurant class"""

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