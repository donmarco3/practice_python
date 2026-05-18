# ask user for string
# print if string is palindrome or not

string = input('Enter a word: ')

if string == string[::-1]:
    print(f'{string} is a palindrome')
else:
    print(f'{string} is not a palindrome')
