cont_game='y'
while(cont_game=='y'):
    player_1=input('Player ONE! Rock, Paper, or Scissors. Choose your play: ').lower()
    player_2=input('Player TWO! Rock, Paper, or Scissors. Choose your play: ').lower()
    if player_1== 'rock' and player_2 == 'rock':
            print('Draw')
    elif player_1== 'rock' and player_2=='paper':
        print('Player 2 wins!')
    elif player_1== 'rock' and player_2=='scissors':
        print('Player 1 wins!')
    elif player_1== 'paper' and player_2 == 'rock':
            print('Player 1 Wins!')
    elif player_1== 'paper' and player_2=='paper':
        print('Draw')
    elif player_1== 'paper' and player_2=='scissors':
        print('Player 2 wins!')
    elif player_1== 'scissors' and player_2 == 'rock':
            print('Player 2 wins!')
    elif player_1== 'scissors' and player_2=='paper':
        print('Player 1 wins!')
    elif player_1== 'scissors' and player_2=='scissors':
        print('Draw.')
    cont_game = input("Do you want to play again? y/n")
