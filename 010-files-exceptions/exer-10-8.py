"""
10-8. Cats and Dogs: Make two files, cats.txt and dogs.txt. Store at least three
names of cats in the first file and three names of dogs in the second file. 
Write a program that tries to read these files and print the contents of the
file to the screen. Wrap your code in a try-except block to catch the
FileNotFound error, and print a friendly message if a file is missing.
Move one of the files to a different location on your system, and make
sure the code in the except block executes properly.
"""

def readit(file):
    """Reads a file and prints its content, with error handling"""
    try:
        with open(file) as f_obj:
            content = f_obj.read()
    except FileNotFoundError:
        print(f'Sorry, "{file}" is missing.')
    else:
        print(f'\n\tContent of {file} is:\n{content}')
    
readit('cats.txt')
readit('dogs.txt')