word = input("Enter a word: ")
print("Your entered word is: ", word)
length = len(word)
if length % 2 == 0:
    char1 = word[length//2 - 1]
    char2 = word[length//2]
    print("Middle characters are: ", char1, char2)

else:
    char = word[length//2]
    print("Middle character is: ", char)