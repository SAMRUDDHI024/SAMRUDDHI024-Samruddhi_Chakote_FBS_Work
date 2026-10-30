# 9. Write a program of having n number of elements in the list and find out even and odd elements in that list and then create two separate lists.

li=[]
n = int(input('enter the no of elements in the list :  '))
for i in range(n):
    a = int(input('enter the element : '))
    li.append(a)

even = []
odd = []
for i in range(n):
    if(li[i] % 2 == 0 ):
        even.append(li[i])
    else:
        odd.append(li[i])

print(f'original list : {li}')
print(f' even list : {even}')
print(f' odd list : {odd}')
