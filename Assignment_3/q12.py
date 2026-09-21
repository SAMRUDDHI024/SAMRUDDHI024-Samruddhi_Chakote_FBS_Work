#12. Write a program to check if given 3 digit number is a palindrome or not.

n = int(input('enter the number : '))
num = n

d1 = n % 10
n = n // 10

d2 = n % 10
n = n // 10

d3 = n % 10
n = n // 10

pal = d1*100 + d2*10 + d3

if(num == pal):
    print(f'number {num} is palindrome number')
else:
    print(f'number {num} is not palindrome number')
