# create a password generator
# ask user how strong they want their password - pick a word from a list

import random

random_passwords = [
    'experience',
    'depression',
    'researcher',
    'reflection',
    'proportion',
    'dictionary',
    'negligence',
    'admiration',
    'background',
    'conference',
    'confession',
    'conviction',
    'chimpanzee',
    'particular',
    'reluctance',
    'difference',
    'deficiency',
    'simplicity',
    'conspiracy',
    'attachment'
]


def generate_password(strength):
    password = ''

    if strength == 'weak':
        password = random_passwords[random.randint(0, 19)]

    else:
        end_range = 10 if strength == 'medium' else 15
        for _ in range(0, end_range):
            password += chr(random.randint(33, 127))

    return password


while True:
    password_strength = input(
        'How strong would you like your password (weak, medium, strong)?: ').lower()
    if password_strength not in ['weak', 'medium', 'strong']:
        print('Must chose either weak, medium, or strong')
    else:
        print(generate_password(password_strength))
        break
