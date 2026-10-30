# 3. Write a program to find the second largest element in the list.

li = []
n = int(input('enter the no of elemets in the list : '))

for i in range(n):
    a = int(input('enter the element : '))
    li.append(a)

max =li[0]
second = None

for i in range(n):
    if(li[i] > max):
        second = max
        max = li[i]
    elif(li[i] < max):
        if(li[i] > second):
            second = li[i]

print(f'the second largest element in the list is : {second}')