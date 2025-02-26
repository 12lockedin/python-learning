"""
9-3. Users: Make a class called User. Create two attributes called first_name
and last_name, and then create several other attributes that are typically 
stored in a user profile. Make a method called describe_user() that prints a 
summary of the user’s information. Make another method called greet_user() that 
prints a personalized greeting to the user.
Create several instances representing different users, and call both methods
for each user.
"""

class User():
    """Storing users attributes and pl wthm"""
    
    def __init__(self, first_name, last_name, age, fav_game, height):
        """Initialize user's data"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.fav_game = fav_game
        self.height = height

    def describe_user(self):
        """Display all user's info"""
        print(f'-----USER INFO-----\n'
              f'- First name: {self.first_name.title()}.\n'
              f'- Last name: {self.last_name.title()}.\n'
              f'- Age: {str(self.age)}.\n'
              f'- Favourite game: {self.fav_game.title()}.\n'
              f'- Height: {self.height}.\n'
              f'-------------------')
        
    def greet_user(self):
        """Greet the user"""
        print(f'Hi there, {self.first_name.title()} {self.last_name.title()}!!!')

u_mike = User('mike', 'arganda', 27, 'RDR2', '191cm')
u_john = User('john', 'garcia', 43, 'super mario bros', '172cm')
u_carla = User('carla', 'montes', 25, 'rolling over', '169cm')

u_mike.greet_user()
u_mike.describe_user()
print()
u_john.greet_user()
u_john.describe_user()
print()
u_carla.greet_user()
u_carla.describe_user()