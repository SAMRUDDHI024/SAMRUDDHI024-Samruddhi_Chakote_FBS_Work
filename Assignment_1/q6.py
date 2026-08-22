#6. Write a Program to input two angles from user and find third angle of the
# triangle

# Take Input
a1 = int(input('enter the first angle of triangle :'))
a2 = int(input('enter the second angle of triangle :'))

# perform the opration
a3 = 180 - (a1 + a2)

#Display the result
print(f' with angle a1:{a1} and a2:{a2} ,the third angle of trianle is {a3}. ')