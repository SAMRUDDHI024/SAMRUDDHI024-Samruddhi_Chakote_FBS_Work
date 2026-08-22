#10. Write a program to calculate area of an equilateral triangle.

# take the input
side = int(input('enter the side of  equilateral Triangle : '))

# perform opration
# Area = ((3**0.5) / 4 ) * side  * side 
Area = ((3**0.5) / 4 ) * side**2 

#Display the result
print(f'The Area of Equilateral Triangle of side:{side}  is {Area} .')