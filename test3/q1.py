#1. Write a program to print first n prime numbers

n = int(input('enter the number :'))

for i in range(2,n):
    if(n % i== 0):
        print(f'{n} is not prime number .')
        break
else:
    print(f'{n} is  prime number .')


