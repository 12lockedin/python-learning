"""
10-10. Common Words: Visit Project Gutenberg (http://gutenberg.org/ )
and find a few texts you’d like to analyze. Download the text files for these
works, or copy the raw text from your browser into a text file on your
computer.
You can use the count() method to find out how many times a word or
phrase appears in a string. For example, the following code counts the number
of times 'row' appears in a string:
>>> line = "Row, row, row your boat"
>>> line.count('row')
2
>>> line.lower().count('row')
3
Notice that converting the string to lowercase using lower() catches
all appearances of the word you’re looking for, regardless of how it’s
formatted.
Write a program that reads the files you found at Project Gutenberg and
determines how many times the word 'the' appears in each text.
"""

def countit(word_to_count, textname):
    """Count how many times a specific word is repeated in a text file"""
    
    try:
        with open(textname, encoding='utf-8') as file:
            content = file.read()
    except FileNotFoundError:
        print(f'The file {textname} is not found.')
        return 0
    except UnicodeDecodeError:
        print(f'Could not decode {textname}, try a different encoding.')
    else:
        return content.lower().count(word_to_count.lower())

sabotage = 'simple_sabotage.txt'
multitoode = 'theyre_a_multitoode.txt'

books = [sabotage, multitoode]
for book in books:
    count = countit('the', book)
    print(f'The number of "the" in {book} is: {count}')