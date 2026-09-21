#5. WAP to print Fibonacci series upto n. 

n = int(input('enter the number till fibonacii series you want : '))

print('while loop : ')
i = 1
a = -1
b = 1
while( i < n+1):
    c = a+b
    print(c , end=' ')
    a = b
    b = c
    i+=1


print(' ')
print('for loop : ')
a = -1
b = 1
for i in range(n):
    c = a + b
    print(c,end=' ')
    a = b
    b = c
    

