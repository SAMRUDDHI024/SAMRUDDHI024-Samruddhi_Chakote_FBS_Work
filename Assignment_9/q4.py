# 4. Write a program to find sum of n numbers using recursion.

def sum(n):
    if(n == 1):
        return 1
    else:
        return n + sum(n-1)

n = int(input('enter the number : '))
print(f'sum of numbers is {sum(n)}')