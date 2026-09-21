#3. WAP to print sum of series upto n. 

n = int(input('enter the number till sum you want : '))

print('while loop : ')
i = 1
sum = 0

while( i < n+1):
    sum += i
    i+=1
print(f'sum of {n} number is : {sum} .')


print('for loop :')
sum = 0
for i in range(1,n+1):
    sum += i
print(f'sum of {n} number is : {sum} .')
