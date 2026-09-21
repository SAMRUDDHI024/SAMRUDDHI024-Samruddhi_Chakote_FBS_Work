#6. Write a program to calculate profit or loss.

sp = int(input('enter the selling price : '))
cp = int(input('enter the cost price : '))
a = sp - cp

if(a > 0):
    print(f'with sp :{sp} and cp :{cp} , profit happen with {a} amount .')
elif(a < 0):
    print(f'with sp :{sp} and cp :{cp} , loss happen with {abs(a)} amount .')
else:
    print(f'with sp :{sp} and cp :{cp} , no profit no loss .')
