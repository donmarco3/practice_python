# generate a random number between 1 and 9 (including)
# ask user to guess the number
# print if they guessed right or wrong

import random

while True:
    random_num = random.randint(1, 9)

    try:
        guess = int(input('Guess a number: '))
    except ValueError:
        print('Must enter a number')
    else:
        if random_num == guess:
            print('Congratulations, you guessed right')
        else:
            print('Bad luck, try again')

        keep_playing = input(
            'If you want to quit playing, type exit: ').lower()
        if keep_playing == 'exit':
            break
