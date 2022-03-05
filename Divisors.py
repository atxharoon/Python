num = input("Please enter an integer")
while(type(num)!=int):
    try:
        num=int(num)
        break
    except ValueError:
        num=input("You did not enter an integer. Please enter an integer: ")
div_list=[]
for divisor in range(1,num+1):
    if num%divisor == 0:
        div_list.append(divisor)
print(div_list)
