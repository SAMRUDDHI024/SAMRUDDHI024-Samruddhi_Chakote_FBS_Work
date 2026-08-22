#2. Convert temp from Celsius to Fahrenheit. (C/5 = (F-32)/9)

# take input 
c =  int(input('enter the temperature in celsius : '))

# perform opration
f = ((9/5) * c) + 32

# display result
print(f'the temperature in celsius :{c} is equls to {f} fahrenheit')