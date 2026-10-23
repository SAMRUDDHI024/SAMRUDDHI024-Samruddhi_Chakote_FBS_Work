# 6. Write a program to print Fibonacci series using recursion.

def fibonacci(n, a=1, b=1):
    if(n == 0):
        return
    print(a, end=' ')
    fibonacci(n-1, b, a+b)

n = int(input('how many fibonacci number you want : '))
fibonacci(n)