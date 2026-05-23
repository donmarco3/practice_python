# function that takes 3 variables and returns the largest - with max function

def max(n1, n2, n3):
    max = n1
    for num in [n1, n2, n3]:
        if num > max:
            max = num
    return max


print(max(8, 5, 3))
