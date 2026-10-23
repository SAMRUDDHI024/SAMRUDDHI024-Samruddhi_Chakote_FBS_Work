# 11. WAP to check if a given number is Armstrong number or not. For
# each task create separate functions.

def armstrongNo():
    num = int(input('enter the number : '))

    temp = num
    count = 0
    while(temp > 0):
        count += 1
        temp = temp // 10

    temp = num
    sum = 0
    while(temp > 0):
        d = temp % 10
        temp = temp // 10
        sum = sum + (d ** count)

    if(sum == num):
        print('number is armstrong no')
    else:
        print('number is not armstrong no')

armstrongNo()