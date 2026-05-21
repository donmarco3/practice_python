# randomly generate a 4 digit number
# if user guesses number in correct position -> cow else bull
# return how many cows and bulls the user gets
# once the user guesses correctly the game is over

import random


computer_number = []
for _ in range(0, 4):
    computer_number.append(random.randint(0, 9))
print(computer_number)


def compare_numbers(user, computer):
    cows = 0
    bulls = 0

    for i, num in enumerate(computer):
        if num == int(user[i]):
            cows += 1
        else:
            bulls += 1
    print(f'{cows} cows, {bulls} bulls')

    if bulls > 0:
        print('Try again')
    else:
        print('Congratulations! You guessed correctly')
    return cows


while True:
    user_number = list(input('Enter a 4 digit number: '))
    if len(user_number) != 4:
        print('Number must be 4 digits')
    else:
        result = compare_numbers(user_number, computer_number)
        if result == 4:
            break
