# ask the user to guess a letter
# don't let them guess the same letter - keep track of which letters have been guessed

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

while True:
    if letter in guessed_letters:
        letter = ''
        print('Already guessed')
    elif letter in word_list:
        index = word_list.index(letter)
        guessed[index] = letter
        word_list[index] = '_'
    else:
        print(''.join(guessed))
        if letter != '':
            guessed_letters.append(letter)
        letter = input('Guess letter: ').upper()

    if '_' not in guessed:
        print('You won!')
        print(f'The word is {word}')
        break
