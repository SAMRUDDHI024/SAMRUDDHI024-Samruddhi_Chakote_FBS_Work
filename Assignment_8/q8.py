# 8. Write a program find reverse of a number

n = int(input('enter the number : '))
temp = n
rev_num = 0

while(temp > 0):
    d = temp % 10
    temp = temp // 10
    rev_num = rev_num * 10 + d

print(f'reverse of number is {rev_num}')