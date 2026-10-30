# 12. Write a program to create three lists of numbers, their squares and cubes.

li=[]
n = int(input('enter the no of elements in the list :  '))
for i in range(n):
    a = int(input('enter the element : '))
    li.append(a)

s =[]
c  =[]

for i in range(n):
   s.append(li[i] ** 2)
   c.append(li[i] ** 3)

print(f'original list : {li}')
print(f'square  list : {s}')
print(f'cube  list : {c}')