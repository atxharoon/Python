from random import randint
import sys

#Generating random lists of size 20 and findng the intersection. 
list_a = [randint(1, 10) for p in range(randint(1,20))]
list_b = [randint(1, 10) for p in range(randint(1,20))]
print(list(set(list_a).intersection(list_b)))


#Second method to find intersection of two lists. 
c=[]
for ind in range(len(list_a)):
        if list_a[ind] in list_b:
            if list_a[ind] not in c:
                c.append(list_a[ind])
print(c)