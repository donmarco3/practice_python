# save the dict from the previous exercise to a json file on disk

import json

birthdays = {
    'Albert Einstein': '03/14/1879',
    'Benjamin Franklin': '01/17/1706',
    'Ada Lovelace': '12/10/1815',
    'Donald Trump': '06/14/1946',
    'Rowan Atkinson': '01/6/1955'
}

with open('birthdays.json', 'w') as f:
    json.dump(birthdays, f)

with open('birthdays.json', 'r') as f:
    birthdays = json.load(f)

name = input('Enter a name: ')
print(f'{name}\'s birthday is {birthdays[name]}')
