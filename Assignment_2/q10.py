#10. Write a program to reverse three-digit number
# take input 
n = int(input('enter the number :'))

# perform opration

d1 = n % 10 
n = n// 10 

d2 = n % 10 
n = n // 10 

d3 = n % 10 
n = n // 10 

# reverce
 #r = d1 + (d2 * 10) + (d3 * 100) # exact number
r =(d1 * 100) + (d2 * 10) + d3  # r = d1*100 + d2*10 +d 3

# display 
print(f'  with number :{n} ,reverce of these digits is {r}')
