"""
6-6. Polling: Use the code in favorite_languages.py (page 104).
•	 Make a list of people who should take the favorite languages poll. Include
some names that are already in the dictionary and some that are not.
•	 Loop through the list of people who should take the poll. If they have
already taken the poll, print a message thanking them for responding.
If they have not yet taken the poll, print a message inviting them to take
the poll.
"""
poll_takers = ['jen', 'scarlett', 'sarah', 'edward', 'lucy', 'phil']

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " + language.title() + ".")

print('\n')
for name in poll_takers:
    if name in favorite_languages.keys():   # This can be used without .keys()
        print(f'Thank you, {name.title()} for taking the poll.\n')
    else:
        print(f'{name.title()}, you should take the poll.\n')