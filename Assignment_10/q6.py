# 6. Write a program to remove duplicates from the list.

li=[]
n = int(input('enter the no of elements in the list :  '))
for i in range(n):
    a = int(input('enter the element : '))
    li.append(a)

li2 = []
for i in range(n):
    if(li[i] not in li2):
        li2.append(li[i])

print(f'list after removing duplicates is {li2}')