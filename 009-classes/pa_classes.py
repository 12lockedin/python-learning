"""Only Privilege and Admin classes"""

from u_class import User

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