"""
10-1. Learning Python: Open a blank file in your text editor and write a few
lines summarizing what you’ve learned about Python so far. Start each line
with the phrase In Python you can.... Save the file as learning_python.txt in the
same directory as your exercises from this chapter. Write a program that reads
the file and prints what you wrote three times. Print the contents once by reading in the entire file, once by looping over the file object, and once by storing
the lines in a list and then working with them outside the with block.
"""

filename = 'learning_python.txt'

# Method 1: Reading the entire file at once
print("Method 1: Reading entire file at once")
with open(filename, 'r') as file:
    contents = file.read()
    print(contents)

# Method 2: Looping over the file object
print("\nMethod 2: Looping over file object")
with open(filename, 'r') as file:
    for line in file:
        print(line.strip())  # strip() removes extra newline characters

# Method 3: Storing lines in a list
print("\nMethod 3: Storing lines in a list")
with open(filename, 'r') as file:
    lines = file.readlines()

# Print lines from the list
for line in lines:
    print(line.strip())


"""
import os

# Print current working directory
print("Current working directory:", os.getcwd())

# Print full path to the file you're trying to open
filename = 'learning_python.txt'
full_path = os.path.abspath(filename)
print("Full path to file:", full_path)

# Check if file exists
print("File exists:", os.path.exists(full_path))

# List files in the current directory
print("\nFiles in current directory:")
print(os.listdir())
"""