#exercise 3-10: create a list of whatever and use every function in this chapter at least once
stocks = ['AAPL', 'NVIDIA', 'META', 'GOOG', 'TSLA', 'AMZN', 'NET']

#accessing elements in a list
print('The mst valuable is: ' + stocks[1])

#Title cases, changes teomporarly
print('using .title(): ' + stocks[1].title())

#accessing the last element
print('last element: ' + stocks[-1])

#modifying elements on a list
stocks[0] = 'NFLX'
print('first element changed:\n' + str(stocks))

#appending elements to end of a list
stocks.append('AAPL')
print('.append("AAPL"):\n' + str(stocks))

#we can create lists dynamically
new_l=[]
new_l.append('ave')
new_l.append('maria')
print(new_l)

#insterting elements into a list
stocks.insert(0, 'BRK.B')
stocks.insert(1, 'OXY')

print(stocks)

#deleting elements form a list, YOU MUST KNOW THE POSITON
print('\ndel stocks.[1]')
del stocks[1]
print(stocks)

#using .pop() to use a value before deleting it
print('stocks.pop():\n\t' + stocks.pop() + '\n\t' + str(stocks))
#popping form any position
print('stocks.pop(0):\n\t' + stocks.pop(0) + '\n\t' + str(stocks))

#using remove to quit an element without knowing its position
overpriced = 'TSLA'
stocks.remove(overpriced)
print('\nstocks.remove("TESLA"):\n\t' + str(stocks))

#sort by alphabetical order
#temporarily
print('\nsorted(stocks): ' + str(sorted(stocks)))
print('stocks: ' + str(stocks))
#temporarily and reverse
print('\nsorted(stocks, reverse=True): ' + str(sorted(stocks, reverse=True)))
print('stocks: ' + str(stocks))
#permanently
stocks.sort()
print('stocks using(stocks.sort()): ' + str(stocks))
#permanently and reversed
stocks.sort(reverse=True)
print('stocks using(stocks.sort(reverse=True)): ' + str(stocks))

#permanently reversing
stocks.reverse()
print('stocks using(stocks.reverse(): ' + str(stocks))

#length of a list
print('length: ' + str(len(stocks)))