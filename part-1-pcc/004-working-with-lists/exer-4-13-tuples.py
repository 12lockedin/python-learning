#exer-4-13
foods = ('milanesa', 'pasta', 'hamburguesa', 'cocido', 'fabada')

for food in foods:
    print(food)

#foods[0] = 'fruit'      This doesn't work because tuples can't be modified
#Tuples can only be rewritten

foods = ('fruta', 'rape', 'hamburguesa', 'cocido', 'fabada')
print("\nNew food menu:")
for food in foods:
    print(food)
