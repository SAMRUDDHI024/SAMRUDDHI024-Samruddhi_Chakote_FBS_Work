# 10. Write a program to remove all occurrences of a given element in the list
 
li=[]
n = int(input('enter the no of elements in the list :  '))
for i in range(n):
    a = int(input('enter the element : '))
    li.append(a)

num = int(input('enter the number to remove : '))
li2 =[]
for i in range(n):
    if (li[i] != num):
        li2.append(li[i])

print(f'list after removing element is {li2}')

# in same list 
i = 0
while(i < len(li)):
    if(li[i] == num):
        li.pop(i)
    else:
        i += 1

print(f'list after removing element is {li}')

