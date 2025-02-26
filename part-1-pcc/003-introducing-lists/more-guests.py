#exercise 3-6
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