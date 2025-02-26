"""
7-5. Movie Tickets: A movie theater charges different ticket prices depending on
a person’s age. If a person is under the age of 3, the ticket is free; if they are
between 3 and 12, the ticket is $10; and if they are over age 12, the ticket is
$15. Write a loop in which you ask users their age, and then tell them the cost
of their movie ticket.
"""

# Problem: exercise does not define when to exit the loop

message = 'Enter your age: '
error = 'Age must be a number between 0 and a 100. Correct it.'


while True:
    try:
        age = int(input(message))
        if (age < 0) or (age > 100):
            print(error)
            print()
        else:
            if age < 3:
                print('\tYour ticket is free.\n')
            elif age <= 12:
                print('\tYour ticket is 10$.\n')
            else:
                print('\tYour ticket is 15$.\n')
            break
    except:
        print(error)
        print()

# I am advanced so I already know error handling hahah