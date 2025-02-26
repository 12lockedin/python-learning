"""
10-2. Learning C: You can use the replace() method to replace any word in a
string with a different word. Here’s a quick example showing how to replace
'dog' with 'cat' in a sentence:
>>> message = "I really like dogs."
>>> message.replace('dog', 'cat')
'I really like cats.'
Read in each line from the file you just created, learning_python.txt, and
replace the word Python with the name of another language, such as C. Print
each modified line to the screen.
"""

filename = 'learning_python.txt'

# Method 3: Storing lines in a list
print("\nMethod 3: Storing lines in a list")
with open(filename, 'r') as file:
    lines = file.readlines()


# Print lines from the list
i = 0
modified_lines = list(range(len(lines)))
for line in lines:
    print(line.strip())
    modified_lines[i] = line.replace('Python', 'C')
    i += 1
print()

for line in modified_lines:
    print(line.strip())