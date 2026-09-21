#3. Write a program to input angles of a triangle and check whether triangle is valid or not

a1 = int(input('enter the first angle of Triangle : '))
a2 = int(input('enter the second angle of Triangle : '))
a3= int(input('enter the third angle of Triangle : '))

if(a1 + a2 + a3 == 180):
    print(f'Triangle with angles : {a1}, {a2}, {a3} is a Valid triangle')
else:
    print(f'Triangle with angles : {a1}, {a2}, {a3} is a Invalid triangle')