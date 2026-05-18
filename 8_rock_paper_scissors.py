# ask player one for input
# ask player two for input
# compare them
# print congratulations message
# ask if they want to play again

valid_choices = ['rock', 'paper', 'scissors']

while True:
    player1 = input('Player 1: ').lower()
    if player1 not in valid_choices:
        print('Must pick either Rock, Paper, or Scissors')
        continue

    player2 = input('Player 2: ').lower()
    if player2 not in valid_choices:
        print('Must pick either Rock, Paper, or Scissors')
        continue

    if player1 == player2:
        print('It\'s a tie')
    elif player1 == 'rock' and player2 == 'scissors' or player1 == 'scissors' and player2 == 'paper':
        print('Player 1 wins')
    else:
        print('Player 2 wins')

    play_again = input('Do you want to play again? (y / n): ')
    if (play_again == 'n'):
        break
