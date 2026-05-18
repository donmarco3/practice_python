# print all elements in list that are less than ten

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

for num in a:
    if num < 10:
        print(num)

print([num for num in a if num < 10])
