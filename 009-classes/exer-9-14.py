"""
9-14. Dice: The module random contains functions that generate random numbers
in a variety of ways. The function randint() returns an integer in the
range you provide. The following code returns a number between 1 and 6:
from random import randint
x = randint(1, 6)
Make a class Die with one attribute called sides, which has a default
value of 6. Write a method called roll_die() that prints a random number
between 1 and the number of sides the die has. Make a 6-sided die and roll
it 10 times.
Make a 10-sided die and a 20-sided die. Roll each die 10 times.
"""

from random import randint

class Die:
    """Die generator"""

    def __init__(self, sides=6):
        """Initialize sides, by default 6"""
        self.sides = sides
        self.runs = 10

    def roll_die(self):
        """Roll the dice"""
        return randint(1,self.sides)

    def ten_runs(self):
        """Roll the dice 10 times"""
        # This was unnecesary but I did it just because
        print(f'-----ROLLING YOUR {self.sides} DIE-----')
        for i in range(self.runs):
            print(f'-> {self.roll_die()}')
        print(f'///////////////////////////////////////')

# 6 sided die

six_die = Die(6)
ten_die = Die(10)
twenty_die = Die(20)

six_die.ten_runs()
ten_die.ten_runs()
twenty_die.ten_runs()