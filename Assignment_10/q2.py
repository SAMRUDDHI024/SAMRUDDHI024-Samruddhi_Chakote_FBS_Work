# 2. Write a program to find maximum and minimum element in a list.

li = []
n = int(input('enter the number of elements in the list : '))

for i in range(n):
    a = int(input('enter the element : '))
    li.append(a)

min = li[0]
max = li[0]

for i in range(n):
    if(li[i]< min):
        min = li[i]

    if(li[i] > max):
        max = li[i]

print(f'min = {min}  and    max = {max}')