"""
10-4. Guest Book: Write a while loop that prompts users for their name. When
they enter their name, print a greeting to the screen and add a line recording
their visit in a file called guest_book.txt. Make sure each entry appears on a
new line in the file.
"""

filename = 'guest_book.txt'

with open(filename, 'a') as file:
    while True:
        name = input("Hello!!! YOUR NAME: ")
        if name == 'q':
            break
        else: 
            file.write(f'{name}\n')