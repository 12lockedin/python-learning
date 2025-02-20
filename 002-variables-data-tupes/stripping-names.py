#Exercise 2-7 Stripping Names: Store a person's name, and include some whitespace characters at the beginning and end of the name. Make sure you use each character combination, "\t" and "\n", at least once.

name = ' Johann Sebastian Bach '
print(name + '\n"' + name.strip() + '"\n\t"' + name.lstrip() + '"\n\t"' + name.rstrip() + '"')