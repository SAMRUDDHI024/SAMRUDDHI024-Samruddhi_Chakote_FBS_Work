#8. Write a program to convert days into years, weeks and days

# take input
days = int(input('enter number of days : '))

# calculate years, weeks and days
years = days // 365
r_days = days % 365
print(r_days)

weeks = r_days // 7
r_days = r_days % 7

# display result
print(f'In {days} days there are {years} years, {weeks} weeks and {r_days} remaining days')
