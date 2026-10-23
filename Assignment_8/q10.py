# 10. Write a program to check if entered year is a leap year or not.

year = int(input('enter the year : '))

if(year % 400 == 0):
    print('the year is leap year')
elif(year % 100 == 0):
    print('the year is not leap year')
elif(year % 4 == 0):
    print('the year is leap year')
else:
    print('the year is not leap year')