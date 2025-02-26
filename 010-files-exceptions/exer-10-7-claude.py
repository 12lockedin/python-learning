
"""
10-7. Addition Calculator: Wrap your code from Exercise 10-6 in a while loop
so the user can continue entering numbers even if they make a mistake and
enter text instead of a number
"""
print('Hello! I will sum any two numbers!')
print('Type "q" to quit at any time.')

while True:
    # Get first number
    num1 = input('\tGive me number 1: ')
    if num1.lower() == 'q':
        break
        
    # Get second number
    num2 = input('\tGive me number 2: ')
    if num2.lower() == 'q':
        break
    
    # Try to convert and add numbers
    try:
        num1_int = int(num1)
        num2_int = int(num2)
        num_sum = num1_int + int(num2)
        print(f'-> {num_sum}')
    except ValueError:
        print('YOU MUST GIVE ME A NUMBER! Let\'s try again.')
        # No break here so the loop continues

print('Thanks for using the calculator!')