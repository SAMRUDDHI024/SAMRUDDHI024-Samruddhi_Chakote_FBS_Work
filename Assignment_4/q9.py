#9. WAP to print all numbers in a range divisible by a given number

r1 = int(input('enter the lowest Range : '))
r2 = int(input('enter the highest Range : '))
n = int(input('enter the number whose divisible number you want : '))

for i in range(r1 , r2+1):
    if(i % n == 0):
        print(i)