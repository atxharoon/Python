user_int=int(input('Please enter an integer: '))
def primeornot(numbertotest):
    if (numbertotest%2==0 and numbertotest!=2) or numbertotest==1:
        print(f'{numbertotest} is not prime')
    else: 
        divisors=[]
        for i in range(3,numbertotest,2):
            if numbertotest%i==0:
                divisors.append(i)
        if len(divisors)==0:
            print(f'{numbertotest} is prime')
        else:
            print(f'{numbertotest} is not prime, the following is a list of all divisors of {numbertotest} other than 1 and itself: ',divisors)
primeornot(user_int)