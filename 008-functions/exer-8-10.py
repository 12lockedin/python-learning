"""
8-10. Great Magicians: Start with a copy of your program from Exercise 8-9.
Write a function called make_great() that modifies the list of magicians by
adding the phrase the Great to each magician’s name. Call show_magicians() to
see that the list has actually been modified.
"""

def show_magicians(mags):
    """Present each magician"""
    for mag in mags:
        print(f'Hello magician {mag.title()}!')

def make_great(mags):
    """Add greatness to each magician"""
    # The way we are doing it modifies de original list
    for i in range(len(mags)):
        mags[i-1] = 'The Great ' + mags[i-1]


magicians = ['javichy', 'pop', 'copperfield', 'messi']
show_magicians(magicians)
print(f'Now they are great!\n')
make_great(magicians)
show_magicians(magicians)

