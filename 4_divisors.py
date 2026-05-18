# ask user for number
# print out all the divisors of the number

number = int(input('Enter a number: '))
list_range = list(range(1, number + 1))
for num in list_range:
    if number % num == 0:
        print(num)
