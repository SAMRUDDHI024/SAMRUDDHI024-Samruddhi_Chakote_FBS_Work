#7. Program to Find the Roots of a Quadratic Equation

# take input
a = int(input('enter a : '))
b = int(input('enter b : '))
c = int(input('enter c : '))

# perform the opration
d = b**2 - 4*a*c   # discriminant

# calculate roots
r1 = (-b + d**0.5) / (2*a)
r2 = (-b - d**0.5) / (2*a)

# display result
print(f'with Quadratic Equation {a}x**2 +({b}x)+{c} the roots are r1:{r1} and r2:{r2}')
print(f'root 1 is {r1}')
print(f'root 2 is {r2}')