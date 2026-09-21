#4. Write a program to input all sides of a triangle and check whether triangle is valid or
#   not.

s1 = int(input('enter the length of side 1 of triangle : '))
s2 = int(input('enter the length of side 2 of triangle : '))
s3 = int(input('enter the length of side 3 of triangle : '))

if(s1+s2 > s3 and s2+s3 > s1 and s1+s3 >s2):
    print(f'Triangle with sides :{s1}, {s2}, {s3} is a Valid Triangle .')
else:
    print(f'Triangle with sides :{s1}, {s2}, {s3} is a Invalid Triangle .')