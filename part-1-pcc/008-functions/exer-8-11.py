"""
8-11. Unchanged Magicians: Start with your work from Exercise 8-10. Call the
function make_great() with a copy of the list of magicians’ names. Because the
original list will be unchanged, return the new list and store it in a separate 
list. Call show_magicians() with each list to show that you have one list of the
original names and one list with the Great added to each magician’s name.
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
    return mags


magicians = ['javichy', 'pop', 'copperfield', 'messi']
show_magicians(magicians)
print(f'Now they are great!\n')
g_magicians = make_great(magicians[:])

print(f'The normal magicians:')
show_magicians(magicians)

print(f'The g_magicians:')
show_magicians(g_magicians)