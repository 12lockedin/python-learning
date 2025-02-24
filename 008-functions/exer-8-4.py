"""
8-4. Large Shirts: Modify the make_shirt() function so that shirts are large
by default with a message that reads I love Python. Make a large shirt and a
medium shirt with the default message, and a shirt of any size with a different
message.
"""

def make_shirt(size='L', message='I love Python'):
    """Summarizes the information about the shirt"""
    print(f'Size: {size}')
    print(f'Message: {message}')

make_shirt()
make_shirt(size='M')
make_shirt('M', 'I LOVE GELATO')
make_shirt(message='TAY TAY FTW', size='L')