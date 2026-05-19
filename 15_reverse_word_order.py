# ask the user for a long string containing multiple words
# print the words in reverse order

def reverse_string(sen):
    return ' '.join(sen.split()[::-1])


sentence = input('Write a sentence: ')
print(reverse_string(sentence))
