#exercise 2-9

fav_number = 8
message = "My favourite number is " + str(fav_number) + "!"
print(message)
print(fav_number) #this will print the number 8
print(str(fav_number)) #this will print the string 8

#This would give an error because you can't concatenate a string with a number
#print("My favourite number is " + fav_number + "!")