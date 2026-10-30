# 4. Write a program to reverse the list.
li = []
n = int(input('enter the no of elements in the liist : '))
for i in range(n):
    a = int(input('enter the element : '))
    li.append(a)

rev = []
for i in range(n-1,-1,-1):
    rev.append(li[i])
print(f'reveresed list is {rev}')


# without using second list 
for i in range(n//2):
    temp = li[i]
    li[i] = li[n-1-i]
    li[n-1-i]  = temp
print(f'reveresed list is {li}')