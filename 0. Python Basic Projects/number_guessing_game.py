'''
Number Guessing Game is a game in which the computer randomly selects a number between 1 and 100. 
The user must guess the number within a limited number of attempts. After each incorrect guess, 
the program provides a hint indicating whether the guess is too low or too high.
(GeeksforGeeks)
'''

import random

number = random.randrange(1, 100, 1)
print(number)

attemps = 7

while True:
    for i in range(1, attemps):
        print(f'Attemp [{i}] of [{attemps}]')
        user_number = input('Please enter a number: ')
        if user_number.isdigit():
            print('It is a number!')
            break
        else:
            i =- 1
            print('it is not a number!')
            continue

