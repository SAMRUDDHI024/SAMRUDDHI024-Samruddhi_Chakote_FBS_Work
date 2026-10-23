#6. Write a program to find print the following Fibonacci series using
# functions:
#  1 1 2 3 5 8 n terms

def fibonacci():
    n = int(input('how many fibonacci number you want : '))
    a = -1
    b = 1

    for i in range(n):
        c = a + b
        print(c, end=' ')
        a = b
        b = c

fibonacci()