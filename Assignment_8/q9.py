# 9. Write a program to check if entered number is a palindrome or
# not

n = int(input('enter the number : '))
temp = n
rev_num = 0

while(temp > 0):
    d = temp % 10
    temp = temp // 10
    rev_num = rev_num * 10 + d

if(rev_num == n):
    print('the number is pallindrome')
else:
    print('the number is not pallindrome')