# 5. Python Program to Sort a List According to the Length of the Elements within the list.

li = []
n = int(input('enter the no of elemnts :  '))

for i in range(n):
    a = input('enter the element : ')
    li.append(a)

for i in range(n):
    for j in range(n-1-i):
        if(li[j] > li[j+1]):
            temp = li[j]
            li[j] = li[j+1]
            li[j+1] = temp

print(f'sorted list is {li}')