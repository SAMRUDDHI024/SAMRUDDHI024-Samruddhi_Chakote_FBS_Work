#13. Write a program to input electricity unit charges and calculate total electricity bill
# according to the given condition:
# For first 50 units Rs. 0.50/unit
# For next 100 units Rs. 0.75/unit
# For next 100 units Rs. 1.20/unit
# For unit above 250 Rs. 1.50/unit
# An additional surcharge of 20% is added to the bill

u = int(input('enter electricity used in unit : '))

if(u <= 50):
    bill = u * 0.50
elif(u <= 150):
    bill = 50*0.50 + (u -50)*0.75
elif(u <= 250):
    bill = 50*0.50 + 150*0.75 +(u-150)*1.20
else:
    bill = 50*0.50 + 150*0.75 + 250*1.20 + (u-250)*1.50

sur = bill * 0.20
total_bill = bill + sur
print(f'the total bill for {u} units is :{total_bill}')