#5. WAP to calculate selling price of book based on cost price and discount.

# take input 
cp =int(input('enter the cost price of book : '))
dis = int(input('enter the discount in percentage : '))

# perform the opration
dis_amount = (cp * dis) / 100
sp = cp - dis_amount 

# display result
print(f'with cost price:{cp} and discount:{dis}, The selling price of the book is {sp}')