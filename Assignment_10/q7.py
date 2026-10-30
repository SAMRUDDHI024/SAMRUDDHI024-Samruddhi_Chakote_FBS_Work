# 7. Write a program to create a new list from existing list which contains cube of each number of list.

li=[]
n = int(input('enter the no of elements in the list :  '))
for i in range(n):
    a = int(input('enter the element : '))
    li.append(a)

li2 =[]

for i in range(n):
   li2.append(li[i] ** 3)

print(f'original list : {li}')
print(f'cube  list : {li2}')
