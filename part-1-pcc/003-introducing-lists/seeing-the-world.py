#exercise 3-8: Seeing the world

#list of five places not in alphabetical order and print
places = ['greece', 'silicon valley', 'china', 'japan', 'rome']
print(places)

#print in alphabetical order
print(sorted(places))

#print list again to demonstrate the original list hasn't changed order
print(places)

#print in reverse alphabetical order using sorted()
print(sorted(places, reverse=True))
#using sorted and reverse
#print(sorted(places).reverse())   This would return "None" because .reverse() doesn't owrk like that

#if we use .reverse() we change the order of our list
places.reverse()
print(places)
#reverse again
places.reverse()
print(places)

#using .sort() to changing the list order
places.sort()
print(places)

#using .sort(reverse=True) to change reverse alphabetical order
places.sort(reverse=True)
print(places)