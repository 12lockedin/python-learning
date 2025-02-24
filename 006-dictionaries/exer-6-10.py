"""
6-10. Favorite Numbers: Modify your program from Exercise 6-2 (page 102) so
each person can have more than one favorite number. Then print each person’s
name along with their favorite numbers.
"""

fav_numbers = {
    'Mozart': [3, 6, 9],
    'Bach': [7, 7, 7],
    'Beethoven': [9, 5, 3],
    'Vivaldi': [5, 0, 1, 4],
    'Liszt': [666, 54932475],
}

for name, numbers in fav_numbers.items():
    print(f"{name.title()}'s fav numbers are:")
    for num in numbers:
        print(f'\t{num}')
    print()