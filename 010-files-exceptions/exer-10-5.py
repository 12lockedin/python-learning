"""
10-5. Programming Poll: Write a while loop that asks people why they like
programming. Each time someone enters a reason, add their reason to a file
that stores all the responses.
"""

filename = 'poll.txt'

print('WELCOME TO THE POLL. Type "q" to exit.')
with open(filename, 'a') as poll:
    while True:
        print('Why is it that you like programming?:')
        answer = input()
        if answer.lower() == 'q':
            break
        else:
            poll.write(f'- {answer}.\n')
