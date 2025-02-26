"""
10-11. Favorite Number: Write a program that prompts for the user’s favorite
number. Use json.dump() to store this number in a file. Write a separate 
program that reads in this value and prints the message, “I know your favorite
number! It’s _____.”
"""
import json

fav_num = 'fav_num.json'
with open(fav_num, 'w') as file:
    fav = input("Your favourite number is: ")
    json.dump(fav, file)

print('---second program---')
with open(fav_num) as file:
    fav_b = json.load(file)
    print(f'I remember! Your favourite number is {fav_b}')

