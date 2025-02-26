"""
10-9. Silent Cats and Dogs: Modify your except block in Exercise 10-8 to fail
silently if either file is missing.
"""

def readit(file):
    """Reads a file and prints its content, with error handling"""
    try:
        with open(file) as f_obj:
            content = f_obj.read()
    except FileNotFoundError:
        pass # Just change the print statement for "pass"
    else:
        print(f'\n\tContent of {file} is:\n{content}')
    
readit('cats.txt')
readit('dogs.txt')