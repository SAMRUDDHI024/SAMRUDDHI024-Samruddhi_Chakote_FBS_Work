# 1. Write a program to find sum of following series using recursive functions:
# 1! + 2! + 3! + 4! + ..... + n!

def fact(n):
    if(n == 1):
        return 1
    else:
        return n * fact(n-1)

def sum(n):
    if(n == 1):
        return 1
    else:
        return fact(n) + sum(n-1)

n = int(input('enter the number : '))
print(f'sum of series is {sum(n)}')