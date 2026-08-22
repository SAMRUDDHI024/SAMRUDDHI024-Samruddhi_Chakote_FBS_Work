#4. Write a program to enter P, T, R and calculate simple Interest.

#Take the Input 
p = int(input('enter the priciple amount :'))
t = int(input('enter the time : '))
r = int(input('enter the Rate : '))

# perform the opration
si = (p * t * r) / 100

# disply the result
print(f'the Simple interest of principle amount :{p}, time:{t} and rate:{r}  is {si} .')

