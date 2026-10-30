# 6. Python Program to Find the Union of two Lists.

li1 =[]
li2 = []
n = int(input('enter the no of elemets in the first list : '))

for i in range(n):
    a = int(input('enter the element : '))
    li1.append(a)

m = int(input('enter the no of elemets in the second list : '))

for i in range(m):
    a = int(input('enter the element : '))
    li2.append(a)


union = []

for i in range(n):
    if(li1[i] not in union ):
        union.append(li1[i])

i=0

for i in range(n):
    if(li2[i] not in union ):
        union.append(li2[i])

print(f'union of two lists is {union}')