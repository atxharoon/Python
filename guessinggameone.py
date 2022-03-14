from random import *
randoint=randint(1,9)
i_1=input('Guess the randomly generated integer from 1 to 9: ')
guess=int(i_1)
counter=1
while(i_1 != 'exit'):
    if guess > randoint:
        print('You guessed too high')
    elif guess < randoint:
        print('You guessed too low')
    i_1=input('Guess the randomly generated number between 1 and 9: ').lower()
    if i_1 =='exit':
        break
    guess = int(i_1)
    counter +=1
    if guess ==randoint:
        print(f'You got it! The number was {randoint}. It took you {counter} tries to guess correctly.')
print('Game Over.')