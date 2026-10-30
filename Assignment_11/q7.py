# 7. Python Program to Find the Intersection of Two Lists.

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

intersection = []

for i in range(n):
    if(li1[i] in li2 and li1[i] not in intersection):
        intersection.append(li1[i])

print(f'intersection of two lists is {intersection}')