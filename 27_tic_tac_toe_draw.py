# draw X for player 1 and 0 for player 2

def check_winner(matrix):
    col1 = list(set([row[0] for row in matrix]))
    col2 = list(set([row[1] for row in matrix]))
    col3 = list(set([row[2] for row in matrix]))

    row1 = list(set([num for num in matrix[0]]))
    row2 = list(set([num for num in matrix[1]]))
    row3 = list(set([num for num in matrix[2]]))

    diag1 = list(set([matrix[0][0], matrix[1][1], matrix[2][2]]))
    diag2 = list(set([matrix[0][2], matrix[1][1], matrix[2][0]]))

    for item in [col1, col2, col3, row1, row2, row3, diag1, diag2]:
        if item[0] == 0:
            return False
        if len(item) == 1 and item[0 != 0]:
            if item[0] == 1:
                print('Winner is Player1')
                return True
            else:
                print('Winner is Player2')
                return True
    print('There is no winner')
    return True


game = [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]]

while not check_winner(game):
    player1 = input('Player 1 what is your move? ').split(',')
    game[int(player1[0].strip()) - 1][int(player1[1].strip()) - 1] = 1

    print(game[0])
    print(game[1])
    print(game[2])

    player2 = input('Player 2 what is your move? ').split(',')
    game[int(player2[0].strip()) - 1][int(player2[1].strip()) - 1] = 2

    print(game[0])
    print(game[1])
    print(game[2])
