# given a .txt file that has a list of name, count the names and print the result


counter = 0
with open('names_list.txt', 'r') as open_file:
    line = open_file.readline()
    while line:
        counter += 1
        line = open_file.readline()
    print(f'There are {counter} names in this file')
