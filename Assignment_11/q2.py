# 2. Python Program to Merge Two Lists and Sort it.

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

for i in range(m):
    li1.append(li2[i])

print(f'merged list is {li1}')

# print(li1 + li2)

for i in range(len(li1)):
    for j in range(len(li1)-1-i):
        if(li1[j] > li1[j+1]):
            temp = li1[j]
            li1[j] = li1[j+1]
            li1[j+1] = temp

print(f'merged and sorted list is {li1}')

