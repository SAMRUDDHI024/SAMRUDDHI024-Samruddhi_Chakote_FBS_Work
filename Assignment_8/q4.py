#4. Sum of all odd numbers between 1 to n

def addition(n):
    sum = 0
    for i in range(1, n+1):
        if(i % 2 != 0):
            sum += i
    return sum

n = int(input('enter the Number  : '))
res = addition(n)
print(f'sum of odd numbers is : {res}')