string_1=input('Please enter a string: ')
string_2=string_1.lower().replace(" ", "")
storage =''
for ind in range(len(string_2)):
    storage += string_2[-1-ind]
if string_2==storage:
    print(string_1, "is a palindrome!")
else: 
    print(string_1, "is a not palindrome.")