'''
This exercise asks the user for an integer and prints out whether the number is even or odd. If the number is a multiple of 4, then a message will be printed accordingly. To increase the challenge slightly,
the user is asked for two integers (numerator and denominator). If the denominator divides the numerator evenly, we print a message to that effect.
'''

initial_int=input("Please enter an integer: ")

while(type(initial_int)!=int):
    try:
        initial_int=int(initial_int)
        break
    except ValueError:
        initial_int=input("You did not enter an integer. Please enter an integer: ")

remainder = initial_int%2
divbyfour=initial_int%4

if remainder==0:
    if divbyfour==0:
        print(initial_int, 'is even and a multiple of 4.')
    else: 
        print(initial_int, 'is even.')
else:
    print(initial_int, 'is odd.')

#Second half of the program starts below

num_int=input("Please enter a numerator integer: ")

while(type(num_int)!=int):
    try:
        num_int=int(num_int)
        break
    except ValueError:
        num_int=input("You did not enter an integer. Please enter a numerator integer: ")

den_int=input("Please enter a denominator integer: ")

while(type(den_int)!=int):
    try:
        den_int=int(den_int)
        break
    except ValueError:
        den_int=input("You did not enter an integer. Please enter a denominator integer: ")
numdivden=num_int%den_int

if numdivden == 0:
    print(f'{den_int} divides evenly into {num_int}')
else:
    print(f'{den_int} does not divides evenly into {num_int}. The remainder is {numdivden}.')