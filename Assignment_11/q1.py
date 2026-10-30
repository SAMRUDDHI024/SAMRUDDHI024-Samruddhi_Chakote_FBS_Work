# 1. Python Program to Put Even and Odd elements of a List into two Different Lists.

li =[]
n = int(input('enter the no of elemets in the list : '))

for i in range(n):
    a = int(input('enter the element : '))
    li.append(a)

even = []
odd =[]

for i in range(n):
    if(li[i] % 2 == 0):
        even.append(li[i])
    else :
        odd.append(li[i])

print(f'Original List : {li}')
print(f'Even List : {even}')
print(f'Odd List : {odd}')