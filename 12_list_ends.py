# return new list with only first and last elements of given
# write inside of a function

a = [5, 10, 15, 20, 25]


def get_first_and_last(arr):
    return [arr[0], arr[-1]]


print(get_first_and_last(a))
