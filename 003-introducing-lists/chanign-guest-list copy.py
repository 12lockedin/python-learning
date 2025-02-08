#exercise 3-5
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

