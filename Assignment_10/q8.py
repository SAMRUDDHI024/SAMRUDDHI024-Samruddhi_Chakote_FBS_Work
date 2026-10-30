li=[]
n = int(input('enter the no of elements in the list :  '))
for i in range(n):
    a = int(input('enter the element : '))
    li.append(a)

li2 =[]
for i in range(n):
    li2.append(li[i])

print(f'original list : {li}')
print(f'Duplicate  list : {li2}')