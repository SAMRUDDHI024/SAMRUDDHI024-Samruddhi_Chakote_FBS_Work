# 3. Write a program to accept basic salary of n emp. (n should be
# accepted from user). If basic salary is below 20000 then
# da=10%,ta=12% and hra=15% otherwise da=15%,ta=18% and
# hra=20%. Based on this calculate the total salary of each emp
# and also total salary of all emp.

n = int(input('enter number of employee : '))
ts = 0

for i in range(1, n+1):
    bs = int(input(f'enter thje basic salary of emp {i} '))
    if(bs < 20000):
        da = bs * 10 / 100
        ta = bs * 12 / 100
        hra = bs *15/100
    else :
        da = bs * 15 / 100
        ta = bs * 18 / 100
        hra = bs *20 /100


    salary = bs + da+ta+hra
    ts = ts +salary
    print(f'total salary is {i} :{salary}')

print(f'total salary of all emp is : {ts}')


