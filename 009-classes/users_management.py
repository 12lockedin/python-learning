"""Classes to manage all users"""

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

class Privileges():
    """Manage all privileges"""
    def __init__(self):
        self.privileges = ['can add post', 'can delete post', 'can add users',
                           'can delete users']
        
    def show_privileges(self):
        """Show all the privileges"""
        print(f'-----DISPLAYING ALL PRIVILEGES-----')
        for privilege in self.privileges:
            print(f'- {privilege.upper()}.')
        print(f'-----------------------------------')
        

class Admin(User):
    """User with privileges"""

    def __init__(self, first_name, last_name, age, fav_game, height):
        """Initialize varibles"""
        super().__init__(first_name, last_name, age, fav_game, height)
        self.privileges = Privileges()