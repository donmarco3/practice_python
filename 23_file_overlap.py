# given two .txt files that have lists of numbers in them, find the overlapping numbers
# print a list of the overlapping numbers

# prime_numbers = []
# with open('prime_numbers.txt', 'r') as f:
#     line = f.readline()
#     while line:
#         prime_numbers.append(int(line))
#         line = f.readline()

# happy_numbers = []
# with open('happy_numbers.txt', 'r') as f:
#     line = f.readline()
#     while line:
#         happy_numbers.append(int(line))
#         line = f.readline()

# overlapping_numbers = []
# for num in prime_numbers:
#     if num in happy_numbers:
#         overlapping_numbers.append(num)

# print(overlapping_numbers)


def file_to_list(file):
    new_list = []
    with open(file) as f:
        line = f.readline()
        while line:
            new_list.append(int(line))
            line = f.readline()
    return new_list


prime_numbers = file_to_list('prime_numbers.txt')
happy_numbers = file_to_list('happy_numbers.txt')


overlapping_numbers = [num for num in prime_numbers if num in happy_numbers]
print(overlapping_numbers)
