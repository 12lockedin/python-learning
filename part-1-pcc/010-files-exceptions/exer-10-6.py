"""
10-6. Addition: One common problem when prompting for numerical input
occurs when people provide text instead of numbers. When you try to convert
the input to an int, you’ll get a TypeError. Write a program that prompts for
two numbers. Add them together and print the result. Catch the TypeError if
either input value is not a number, and print a friendly error message. Test your
program by entering two numbers and then by entering some text instead of a
number.
"""

print('Hello! I will sum any two numbers!')
try:
    num1 = int(input('\tGive me number 1: '))
    num2 = int(input('\tGive me number 2: '))
except (TypeError, ValueError):
    print('YOU MUST GIVE ME A NUMBER!')
else:
    num_sum = num1 + num2
    print(f'-> {num_sum}')