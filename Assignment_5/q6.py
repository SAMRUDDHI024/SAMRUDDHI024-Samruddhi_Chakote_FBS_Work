#6. Write a program to print first n prime numbers. 

n= int(input('enter the  first n prime number :  '))
c = 0
num=2
while(n > c):
    for i in range(2,num): 
            if(num % i == 0):    
                    break
    else:
        print(num , end=' ')
        c += 1
    num+=1