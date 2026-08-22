#11. Write a program to accept an integer amount from user and tell minimum
#number of notes needed for representing that amount. 


# take input
a = int(input('enter the amount : '))

# perfrom opration 
# take std notes like 500,200,100,50,10
n1 = a // 2000
a = a % 2000

n2 = a // 500
a = a % 500

n3 =  a //200
a = a %200 

n4 = a //100
a = a % 100 

n5 =  a //50
a = a % 50 

n6 =  a //20
a = a % 20

n7 =  a //10
a = a % 10

total_notes = n1 + n2 + n3 + n4 + n5 + n6 + n7

# diaply
print(f'notes are for  2000 :{n1}, 500:{n2}, 200:{n3}, 100:{n4}, 50:{n5}, 20:{n6} and 10:{n7}')

print(f' so total notes need  :{total_notes}')

