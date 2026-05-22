# check who has one a game of tic tac toe
# 0 - empty, 1 - player1, 2 - player2

winner_is_2 = [[2, 2, 0],
               [2, 1, 0],
               [2, 1, 1]]

winner_is_1 = [[1, 2, 0],
               [2, 1, 0],
               [2, 1, 1]]

winner_is_also_1 = [[0, 1, 0],
                    [2, 1, 0],
                    [2, 1, 1]]

no_winner = [[1, 2, 0],
             [2, 1, 0],
             [2, 1, 2]]

also_no_winner = [[1, 2, 0],
                  [2, 1, 0],
                  [2, 1, 0]]


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
        if len(item) == 1 and item[0 != 0]:
            if item[0] == 1:
                print('Winner is Player1')
                return
            else:
                print('Winner is Player2')
                return
    print('There is no winner')
    return


check_winner(winner_is_1)
