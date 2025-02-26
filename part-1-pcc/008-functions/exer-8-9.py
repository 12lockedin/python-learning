"""
8-9. Magicians: Make a list of magician’s names. Pass the list to a function
called show_magicians(), which prints the name of each magician in the list.
"""

def show_magicians(mags):
    for mag in mags:
        print(f'Hello magician {mag.title()}!')

magicians = ['javichy', 'pop', 'copperfield', 'messi']
show_magicians(magicians)