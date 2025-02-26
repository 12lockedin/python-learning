"""
10-7. Addition Calculator: Wrap your code from Exercise 10-6 in a while loop
so the user can continue entering numbers even if they make a mistake and
enter text instead of a number
"""
print('Hello! I will sum any two numbers!')
print('Type "q" to quit')

while True:
        num1 = input('\tGive me number 1: ')
        if num1.lower() == 'q':
            break
        else:
            num2 = input('\tGive me number 2: ')
            if num2.lower() == 'q':
                break
            else:
                try:
                    num_sum = int(num1) + int(num2)
                except (TypeError, ValueError):
                    print('YOU MUST GIVE ME A NUMBER!')
                else:
                    print(f'-> {num_sum}')