#1. Write a program to calculate area of rectangle

def calArea(length, breadth):
    area = length * breadth
    return area


length = int(input('enter the length : '))
breadth = int(input('enter the breadth : '))
res = calArea(length, breadth)
print(f'Area of rectangle : {res}')