#9. Write a program to enter base and height of a triangle and find its area.

# take the input
height= int(input('enter the height of Triangle : '))
base = int(input('enter the base of Triangle : '))

# perform opration
Area = (height * base) * 0.5

#Display the result
print(f'The Area of Triangle of height:{height} and Base:{base} is {Area} .')