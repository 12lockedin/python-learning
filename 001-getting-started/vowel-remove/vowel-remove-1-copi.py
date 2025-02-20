word = input("Enter a word: ")
vowels = "aeiou"
new_word = ""
for letter in word:
    if letter not in vowels:
        new_word += letter
print(new_word)
