"""
9-12. Multiple Modules: Store the User class in one module, and store the
Privileges and Admin classes in a separate module. In a separate file, create
an Admin instance and call show_privileges() to show that everything is still
working correctly.
"""
from pa_classes import Admin

pedro_admin = Admin('Pedro', 'Pedro', 57, 'tethered', '190cm')
pedro_admin.privileges.show_privileges()