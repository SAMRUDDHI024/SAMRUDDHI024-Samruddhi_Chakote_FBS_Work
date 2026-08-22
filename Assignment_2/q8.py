# 8. Write a program to swap two numbers using third variable

# take input
x = int(input('enter the num 1 :'))
y = int(input('enter the num 2 :'))
print(f'Befor swapping x:{x} and y:{y}')

# perform opration
z = y 
y = x 
x = z

# display result
print(f'After swapping x:{x} and y:{y}')