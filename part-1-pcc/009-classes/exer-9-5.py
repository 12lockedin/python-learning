"""
9-5. Login Attempts: Add an attribute called login_attempts to your User
class from Exercise 9-3 (page 166). Write a method called increment_
login_attempts() that increments the value of login_attempts by 1. Write
another method called reset_login_attempts() that resets the value of login_
attempts to 0.
Make an instance of the User class and call increment_login_attempts()
several times. Print the value of login_attempts to make sure it was incremented
properly, and then call reset_login_attempts(). Print login_attempts again to
make sure it was reset to 0.
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
        self.login_attempts = 0

    def increment_login_attempts(self):
        """Increment login attempts by 1"""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Reset login attempts to 0"""
        self.login_attempts = 0

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
        print(f'Hi there, {self.first_name.title()} {self.last_name.title()}!!')

my_user = User('manolo', 'muelle', 62, 'break & repair', '178cm')

print(f'initial attempts: {my_user.login_attempts}')
print('--------')
my_user.increment_login_attempts()
print(f'attempts: {my_user.login_attempts}')
print('--------')
my_user.increment_login_attempts()
my_user.increment_login_attempts()
my_user.increment_login_attempts()
print(f'attempts: {my_user.login_attempts}')
print('--------')
for i in range(38):
    my_user.increment_login_attempts()
print(f'attempts: {my_user.login_attempts}')
print('--------')
my_user.reset_login_attempts()
print(f'attempts: {my_user.login_attempts}')
print('--------')