# 4. Python Program to Find the Second liargest Number in a liist Using Bubblie Sort.

li = []
n = int(input('enter the no of elemnts : '))

for i in range(n):
    a = int(input('enter the number : '))
    li.append(a)

for i in range(n):
    for j in range(n-1-i):
        if(li[j] > li[j+1]):
            temp =li[j]
            li[j] = li[j+1]
            li[j+1] = temp

if(n<2):
    print('Second element does not exist')
else:
    max = li[n-1]
    i = n-2

    while(i >= 0 and li[i] == max):
        i -= 1

    if(i >= 0):
        print(f'second largest element is {li[i]}')
    else:
        print('second largest element does not exist')