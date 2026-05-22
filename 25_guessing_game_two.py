# binary search algorithim to guess the users number between 0 and 100
# print the guessed number
# user responds either too high or too low or correct
# when number is guessed, print how many guesses it took


print('Let\'s play a guessing game')
print('Think of a number and i will try and guess it')
print('After i guess, respond with either l (too low), h (too high), or c (correct)')


def binary_search():
    left = 0
    right = 100
    mid = 50
    counter = 1

    print('\n*** Let\'s play a guessing game ***')
    print('\nThink of a number and i will try and guess it')
    print('\nAfter i guess, respond with either l (too low), h (too high), or y (yes)\n')

    result = input(f'Is {mid} the correct number?: ')
    while result != 'y':
        counter += 1
        if result == 'l':
            left = mid + 1
        else:
            right = mid - 1
        mid = (left + right) // 2
        result = input(f'Is {mid} the correct number?: ')
    print(f'It took {counter} times to guess your number')


binary_search()
