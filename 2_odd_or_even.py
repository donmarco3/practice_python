# ask the user for a number
# print whether number is odd or even

number = input('Enter a number: ')
if int(number) % 2 == 0:
    print(f'The number you chose ({number}) is even')
else:
    print(f'The number you chose ({number}) is odd')
