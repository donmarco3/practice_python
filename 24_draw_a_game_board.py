# ask the user what size game board they want
# draw it for them using print statements

size = int(input('What size game board would you like me to draw?: '))


def print_horiz_line():
    print(' --- ' * size)


def print_vert_line():
    print('|    ' * (size + 1))


for _ in range(size):
    print_horiz_line()
    print_vert_line()
print_horiz_line()
