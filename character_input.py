'''
   This is a simple exercise that uses the input function to take a Name and an age. The goal is to calculate the year of the gregorian calendar of when the 100th year will be given the age entered. 
   Since the input function converts any input to a string, it is possible for the age input to not be an integer. To handle this, I inserted a while loop that is triggered and runs when the type of the age variable is not 
   an integer. Within the while loop, I added the try, except block that checks whether the age variable can be converted into an integer. If the operation is possible, the type of the age variable becomes an int;
   otherwise, the user is prompted to enter an integer over and over, until an integer is entered. Then, the datetime module is used to fetch the current year, which is converted into an int type. The age is subtracted 
   from the current year to get a birth year. From the birth year, we add 100 to get our final result, which is printed in a short sentence displaying the name and year when 100 will be reached
'''
from datetime import date
name = input("Please enter your name: ")
age=input("Please enter your age: ")
while(type(age)!=int):
    try:
        age=int(age)
        break
    except ValueError:
        age=input("You did not enter an integer. Please enter your age as an integer: ")
current_year=int(date.today().strftime('%Y'))
year_of_birth=current_year-age
century=year_of_birth+100
message_to_print=f'{name} you will be 100 in the year {century}.'
print(message_to_print)
