# 2. Write a program to check if given number is Armstrong or not using recursive function.

def count(n):
    if(n == 0):
        return 0
    else:
        return 1 + count(n//10)

def armstrong(n, p):
    if(n == 0):
        return 0
    else:
        d = n % 10
        return (d ** p) + armstrong(n//10, p)

num = int(input('enter the number : '))
p = count(num)

if(armstrong(num, p) == num):
    print('number is armstrong no')
else:
    print('number is not armstrong no')