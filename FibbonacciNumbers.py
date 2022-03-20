num_int=int(input("How many numbers of the Fibonacci Sequence do you want to see? "))
def fibonacci(a):
    if a >=2:
        fiblist=[1,1]
        for i in range(3,a+1):
            fiblist.append(fiblist[i-2] + fiblist[i-3])
    elif a==1: 
        fiblist=[1]
    else:
        fiblist=[]      
    return fiblist
print(fibonacci(num_int))
