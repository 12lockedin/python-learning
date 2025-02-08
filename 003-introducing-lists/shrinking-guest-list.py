#exercise 3-7
guests = ['Ilya Sutskever', 'Mago More', 'NearCyan', 'Buddha']
invitation = ', you are invited to dinner at my place this weekend.'

for guest in guests:
    print(guest + invitation)

failed = 'NearCyan'
print('\n\tThe wannabe guest, ' + failed + ' will not be able to make it, and thus, failed.\n')

new_guest = 'Abuelo'
guests[2] = new_guest

for guest in guests:
    print(guest + invitation)

print("\n\t Wait, there's capacity for more guests\n")

guests.insert(0, 'Abuela')
guests.insert(2, 'Laura :)')
guests.append('Manolo')

for guest in guests:
    print(guest + invitation)

print('\n\tActually, the table will not arrive on time, so I will have to shrink the guest list to 2 persons\n')

cancel = ', due to the unexpected logistic failure of the table, your invitation has been cancelled.'

no_list = [6, 5, 4, 3, 1]
for _ in no_list:
    print('Sorry, ' + guests.pop(_) + cancel)

print('\n')
still_inv = ', you are still invited.'

for guest in guests:
    print(guest + still_inv)
print('\n')

del guests[1]
del guests[0]
print[guests] #print list to check if list is empty, gives an error because you cannot print an empty list.