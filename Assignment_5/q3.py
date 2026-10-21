#3. Accept no. of passengers from user and per ticket cost. Then accept age of each
# passenger and then calculate total amount to ticket to travel for all of them based on
# following condition :
# a. Children below 12 = 30% discount
# b. Senior citizen (above 59) = 50% discount
# c. Others need to pay full. 

n = int(input("Enter number of passengers: "))
t = int(input("Enter ticket cost: "))

total_amount = 0
9
for i in range(1, n + 1):
    age = int(input('Enter age of passenger : '))

    if age < 12:
        amount = t - (t * 30 / 100)

    elif age > 59:
        amount = t - (t * 50 / 100)

    else:
        amount = t

    total_amount = total_amount + amount

print(f'total amount : {total_amount}')