#3. Program to find quotient and remainder of two numbers

#take the input
num = int(input('Enter the Dividend : '))
div = int(input('Enter the Divisor : '))

# perform the opration
quotient = num // div  # whole number so floor division
reminder = num % div   # mod 

# Display the result
print(f'the divident is {num} and divisor is {div} and quotient is {quotient} and remainder is {reminder} of two numbers')

