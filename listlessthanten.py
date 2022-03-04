'''
This exercise works with a python list. Specifically, the user is asked to enter an integer, then a list is iterated over and a list with all elements from the initial list less than the user provided integer is printed. 
'''



a = [1,1,1,2,3,5,8,13,21,34,55,89,100,1000,2344]
b=[]

less_than_int=input("Please enter an integer: ")

while(type(less_than_int)!=int):
    try:
        less_than_int=int(less_than_int)
        break
    except ValueError:
        less_than_int=input("You did not enter an integer. Please enter an integer: ")


for val in range(len(a)):
    if a[val] < less_than_int:
        b.append(a[val])
print(b)
