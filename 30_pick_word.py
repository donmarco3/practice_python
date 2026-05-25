# write a function that picks a random word

import random


def get_random_word():
    words = []
    with open('sowpods.txt') as f:
        line = f.readline()
        while line:
            words.append(line.rstrip())
            line = f.readline()
    return words[random.randint(0, len(words))]


print(get_random_word())
