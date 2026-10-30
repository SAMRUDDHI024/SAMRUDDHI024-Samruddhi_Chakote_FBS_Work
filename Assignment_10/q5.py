# 5. Accept a number from user and check if this element is present in the list or not.
# Also tell how many times it is present in the list.
 
li=[]
n = int(input('enter the no of elements in the list :  '))
for i in range(n):
    a = int(input('enter the element : '))
    li.append(a)

num = int(input('enter the number to check : '))
c = 0
for i in range(n):
    if(li[i] == num):
        c +=1

if(c > 0):
    print(f'number {num} is present in the list annd it occurred {c} times in the list')
else:
    print(f'number {num} is not present in the list')
   

