import random
a=random.sample(range(0,100),10)
def listends(list_ends):
    return [list_ends[0], list_ends[-1]]
print(listends(a))