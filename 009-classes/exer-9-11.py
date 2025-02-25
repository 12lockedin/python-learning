"""
9-11. Imported Admin: Start with your work from Exercise 9-8 (page 178).
Store the classes User, Privileges, and Admin in one module. Create a separate 
file, make an Admin instance, and call show_privileges() to show that
everything is working correctly
"""

from users_management import Admin

pedro_admin = Admin('Pedro', 'Pedro', 57, 'tethered', '190cm')
pedro_admin.privileges.show_privileges()