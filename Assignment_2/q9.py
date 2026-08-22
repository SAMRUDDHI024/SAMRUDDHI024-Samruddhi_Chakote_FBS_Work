#9. Write a program to swap two numbers without using third variable.

# take input
x = int(input('enter the num 1 :'))
y = int(input('enter the num 2 :'))
print(f'Befor swapping x:{x} and y:{y}')

# perform opration
x = x + y
y = x - y
x = x - y

# display result
print(f'After swapping x:{x} and y:{y}')