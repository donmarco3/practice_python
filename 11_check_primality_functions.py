# ask user for a number
# determine whether number is a prime number or not

number = int(input('Enter a number: '))

new_list = [num for num in range(2, number) if number % num == 0]

if number > 1:
    if len(new_list) == 0:
        print('Prime number')
    else:
        print('Not a prime number')
else:
    print('Not a prime number')
