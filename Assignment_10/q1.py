# 1. Write a program to find sum of all elements of list.

li = []
n = int(input('enter the number of elements in the list : '))

for i in range(n):
    a = int(input('enter the number : '))
    li.append(a)

sum = 0 
for i in range(n):
    sum += li[i]

print(f'sum of elemets of list is : {sum}')