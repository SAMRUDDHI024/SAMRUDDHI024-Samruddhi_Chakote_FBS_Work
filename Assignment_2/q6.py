#6. WAP to calculate total salary of employee based on basic, da=10% of basic,
#ta=12% of basic, hra=15% of basic

# take the input
b =int(input('enter the basic :'))

# perform opration 
da = (10 * b) / 100
ta = (12 * b) / 100
hra = (15 * b) / 100

total_salary = b + da + ta + hra

# display result 
print(f' with basic :{b}, da:{da}, ta:{ta} and hra:{hra} , The total salary is {total_salary} . ')