#11. WAP to check if given number Strong Number. 
n = int(input('enter the number : '))
temp = n
sum = 0

while(temp > 0):
    d = temp % 10
    temp = temp // 10
    fact = 1
    for i in range(1 , d +1):
        fact = fact * i
    sum= sum + fact

if(sum== n):
    print(f'the number {n} is strong number')
else:
    print(f'the number {n} is not strong number')
