word = input("Enter a word: ")
vowels = "aeiou"
new_word = ""
for letter in word:
    check = 0
    for vocal in vowels:
        if letter != vocal:
            check += 1
    if check == 5:
        new_word += letter 
print(new_word)
