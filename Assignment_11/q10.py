# 10. Write a program to print list after removing even numbers.

li = []
n = int(input('enter the no of elemnts : '))

for i in range(n):
    a = int(input('enter the number : '))
    li.append(a)

i = 0

while(i < len(li)):
    if(li[i] % 2 == 0):
        li.pop(i)
    else:
        i += 1

print(f'list after removing even numbers is {li}')