"""
8-2. Favorite Book: Write a function called favorite_book() that accepts one
parameter, title. The function should print a message, such as One of my
favorite books is Alice in Wonderland. Call the function, making sure to
include a book title as an argument in the function call.
"""

def favourite_book(book):
    """This function prints a message for the book"""
    print(f'One of my favourite books is: {book}')

my_fav_book = 'Steve Jobs by Walter Isaacson'

favourite_book(my_fav_book)