# only let the user guess 6 times
# let them start a new game

import random


def get_random_word():
    words = []
    with open('sowpods.txt') as f:
        line = f.readline()
        while line:
            words.append(line.rstrip())
            line = f.readline()
    return words[random.randint(0, len(words))]


print('Welcome to Hangman!')
word = get_random_word()
word_list = list(word)
guessed = list('_' * len(word_list))
guessed_letters = []
letter = input('Guess letter: ').upper()
guesses = 1

while True:
    if letter in guessed_letters:
        letter = ''
        print('Already guessed')

    if letter in word_list:
        index = word_list.index(letter)
        guessed[index] = letter
        word_list[index] = '_'
    else:
        print(f'You have {6 - guesses} guesses remaining')
        guesses += 1
        print(''.join(guessed))
        if letter != '':
            guessed_letters.append(letter)
        letter = input('Guess letter: ').upper()

    if '_' not in guessed:
        if guesses > 6:
            print('You lost')
        else:
            print('You won!')
        print(f'The word is {word}')
