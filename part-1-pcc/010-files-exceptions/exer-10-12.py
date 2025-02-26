"""
10-12. Favorite Number Remembered: Combine the two programs from
Exercise 10-11 into one file. If the number is already stored, report the favorite
number to the user. If not, prompt for the user’s favorite number and store it in a
file. Run the program twice to see that it works
"""

import json

fav_num = 'fav_num.json'

try:
    with open(fav_num) as file_a:
        fav_a = json.load(file_a)
        print(f'I remember! Your favourite number is {fav_a}')
except FileNotFoundError:
    with open(fav_num, 'w') as file_b:
        fav_b = input("Tell me your favourite number: ")
        json.dump(fav_b, file_b)



