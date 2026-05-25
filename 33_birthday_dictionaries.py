# create a dictionary of names and birthdays

people_dict = {
    'Marco': '08/04/2003',
    'Domenico': '05/03/1999',
    'Vincent': '20/04/1996'
}

name = input('Enter a name: ')
print(f'{name}\'s birthday is {people_dict[name]}')
