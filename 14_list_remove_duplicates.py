# Write a program (function!) that takes a list and returns a new list that contains all the elements of the first list minus all the duplicates.


def remove_duplicates_lists(arr):
    # function using loop and constructing a list
    new_list = []
    for num in arr:
        if num not in new_list:
            new_list.append(num)
    return new_list


def remove_duplicates_sets(arr):
    # function using sets
    return list(set(arr))


a = [1, 1, 2, 21, 3, 5, 8, 8, 21, 55, 89]
print(remove_duplicates_lists(a))
print(remove_duplicates_sets(a))
