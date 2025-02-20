#exer 4-10 
"""
 Using one of the programs you wrote in this chapter, add several
lines to the end of the program that do the following:
•	 Print the message, The first three items in the list are:. Then use a slice to
print the first three items from that program’s list.
•	 Print the message, Three items from the middle of the list are:. Use a slice
to print three items from the middle of the list.
•	 Print the message, The last three items in the list are:. Use a slice to print
the last three items in the list.
"""

#we start with exercise 4-9
cubes = [num**3 for num in range(1,11)]
print(cubes)

#print the first three items
print('\tThe first three items in the list are:' + str(cubes[:3]))

#print the items from the middle of the list
start = int(len(cubes)/2 - 1)
end = int(start + 3)
print("\tThe items from the middle of the list are:" + str(cubes[start:end]))

#print the last three items
print("\tThe last three items are:" + str(cubes[-3:]))

