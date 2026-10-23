# 8. Write a program to check whether a number is prime or not using recursion.

def prime(n, i=2):
    if(n <= 1):
        return False
    elif(i * i > n):
        return True
    elif(n % i == 0):
        return False
    else:
        return prime(n, i+1)

n = int(input('enter the number : '))

if(prime(n)):
    print('the number is prime')
else:
    print('the number is not prime')