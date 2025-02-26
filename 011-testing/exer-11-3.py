"""
11-3. Employee: Write a class called Employee. The __init__() method should
take in a first name, a last name, and an annual salary, and store each of these
as attributes. Write a method called give_raise() that adds $5000 to the
annual salary by default but also accepts a different raise amount.
Write a test case for Employee. Write two test methods, test_give_
default_raise() and test_give_custom_raise(). Use the setUp() method so
you don’t have to create a new employee instance in each test method. Run
your test case, and make sure both tests pass.
"""

import unittest

class Employee:
    """idk yet"""

    def __init__(self, first_name, last_name, annual_salary):
        """still dk"""
        self.first_name = first_name
        self.last_name = last_name
        self.annual_salary = annual_salary

    def give_raise(self, raise_salary=5000):
        """Raise annual salary"""
        self.annual_salary += raise_salary

class TestEmployee(unittest.TestCase):
    """Test raises"""

    def setUp(self):
        """Store the values we need for testing"""
        self.test_employee = Employee('marc', 'andre', 30000)
    
    def test_give_default_raise(self):
        """Should give 5000 more of annueal salary"""
        self.test_employee.give_raise()
        self.assertEqual(self.test_employee.annual_salary, 
                              35000)
        
    def test_give_custom_raise(self):
        """Given 7000 custom raise, should be 37000"""
        self.test_employee.give_raise(7000)
        self.assertEqual(self.test_employee.annual_salary, 
                              37000)
        
unittest.main()