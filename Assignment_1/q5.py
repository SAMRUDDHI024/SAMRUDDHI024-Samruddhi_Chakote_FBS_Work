#5. Write a program to enter P, T, R and calculate Compound Interest.

# take the input
p = int(input('enter the priciple amount :'))
t = int(input('enter the time : '))
r = float(input('enter the Rate : '))

# perform the opration
# amount = p * (1 + (r /100))**t
# ci =  amount - p
ci =  (p * (1 + (r /100))**t) - p

# disply the result
print(f'the Compound interest of principle amount :{p}, time:{t} and rate:{r}  is {ci} .')
