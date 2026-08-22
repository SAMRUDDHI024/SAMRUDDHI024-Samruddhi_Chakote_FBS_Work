#7. Find the sum of three-digit number
 
# take input 
n = int(input('enter the number :'))

# perform opration

d1 = n % 10 
n = n// 10 

d2 = n % 10 
n = n // 10 

d3 = n % 10 
n = n // 10 

# addition
sum = d1 + d2 + d3


print(f'with number :{n} there are thses digits d1:{d1}, d2:{d2}, d3:{d3}.')
print(f'  with number :{n} ,sum of these digits is {sum}')

