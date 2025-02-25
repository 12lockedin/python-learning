"""
9-6. Ice Cream Stand: An ice cream stand is a specific kind of restaurant. Write
a class called IceCreamStand that inherits from the Restaurant class you wrote
in Exercise 9-1 (page 166) or Exercise 9-4 (page 171). Either version of
the class will work; just pick the one you like better. Add an attribute called
flavors that stores a list of ice cream flavors. Write a method that displays
these flavors. Create an instance of IceCreamStand, and call this method.
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

class IceCreamStand(Restaurant):
    """Type of restaurant"""

    def __init__(self, restaurant_name, cuisine_type):
        """initializeng specific attribute for ice cream"""
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['vanilla', 'chocolate', 'yogurt', 'pistaccio']

    def show_flavors(self):
        """Show all the flavours"""
        print(f'-----DISPLAYING ALL FLAVORS-----')
        for flavor in self.flavors:
            print(f'- {flavor.title()}.')
        print(f'--------------------------------')

the_carballinho = IceCreamStand('the carballinho', 'ice cream')
the_carballinho.show_flavors()
