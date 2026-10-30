# 11. Write a program to print all numbers which are divisible by m and n in the list.
li=[]
n = int(input('enter the no of elements in the list :  '))
for i in range(n):
    a = int(input('enter the element : '))
    li.append(a)

m = int(input('enter the value of m : '))
n = int(input('enter the value of n : '))

for i in range(n):
    if(li[i] % m == 0 and li[i] % n == 0):
        print(li[i])