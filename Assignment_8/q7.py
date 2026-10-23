#7. Write a program to find sum of digits of a number.

n = int (input('enter the number :'))
sum =0
while(n > 0):
    d = n % 10
    # print(d)
    sum += d
    n = n // 10 
print(f'sum of digits of number is {sum}')