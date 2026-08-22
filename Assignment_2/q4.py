#4. WAP to calculate area of triangle and rectangle

# take input 
# for rectangle 
length = int(input('enter the length of rectangle : '))
breadth = int(input('enter the breadth of rectangle : '))

# for triangle
height= int(input('enter the height of Triangle : '))
base = int(input('enter the base of Triangle : '))

# perform opration and display result
Area = length * breadth
print(f'The Area of rectangle of length:{length}, breadth:{breadth} is {Area} .')


Area = (height * base) * 0.5
print(f'The Area of Triangle of height:{height} and Base:{base} is {Area} .')

