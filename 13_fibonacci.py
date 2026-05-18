# ask user how many fibonacci numbers to generate
# return the sequence as a list


def fibonacci(first_num, length):
    fibonacci = []
    if length > 0:
        iterator = 1
        fibonacci.append(first_num)
        fibonacci.append(first_num)
        while (iterator + 1) < length:
            current_num = fibonacci[iterator] + fibonacci[iterator - 1]
            fibonacci.append(current_num)
            iterator += 1
    else:
        fibonacci.append(first_num)
    return fibonacci


length = int(
    input('Enter the length of the fibonacci sequence you would like to generate: '))
first_num = int(
    input('Enter the first number of the fibonacci sequence you would like to generate: '))

print(fibonacci(first_num, length))
