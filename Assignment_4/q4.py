#4. WAP to print factorial of a number . 

n = int(input('enter the number whoes factorial number you want : '))

print('while loop :')
i = 1
f = 1
while( i < n+1):
    f *= i
    i += 1
print(f'factorial of {n} : {f}')

print('for loop : ')
f=1
for i in range(1,n+1):
    f *= i
print(f'factorial of {n} : {f}')