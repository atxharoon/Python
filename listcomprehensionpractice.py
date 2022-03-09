a = [89, 4, 78, 16, 75, 36, 49, 64, 861, 100000]
b=[a[i] for i in range(len(a)) if a[i]%2==0]
print(b)