sample_list=[1,2,3,2,3,4,4,4,5,6,7,8,9,13,25,55,55,55,55,45,40,62]
def removeDuplicate(a):
    return list(set(a))
print(removeDuplicate(sample_list))

def removeDuplicateList(a):
    newlist=[]
    for i in a:
        if i not in newlist:
            newlist.append(i)
    return newlist
print(removeDuplicateList(sample_list))