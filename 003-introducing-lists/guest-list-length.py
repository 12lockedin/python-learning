#exercise 3-9, using list from 3-4
guests = ['Ilya Sutskever', 'Mago More', 'NearCyan', 'Buddha']
invitation = ', you are invited to dinner at my place this weekend.'

for guest in guests:
    print(guest + invitation)

#print number of invetees using len(), also necessary to use str() to convert from integer to str()
print('Number of invetees: ' + str(len(guests)))