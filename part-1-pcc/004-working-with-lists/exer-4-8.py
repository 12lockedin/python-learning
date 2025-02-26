#exer-4-8 Make a list of the first 10 cubes (that
#is, the cube of each integer from 1 through 10), and use a for loop to print out
#the value of each cube.

first_cubes = []

#generate the list with each cube
for _ in range(1,11):
    first_cubes.append(_**3)
print("\n")

#print the list
for cube in first_cubes:
    print(cube)
