#2. WAP to print all odd numbers until n. 

n = int(input('enter the number till odd number you want : '))
print('while loop')
i = 1
while(i < n+1):
    if(i % 2 != 0):
        print(i , end=' ')
    i +=1

print(' ')
print('for loop')

for i in range(1,n+1):
    if(i % 2 != 0):
        print(i ,end=' ')