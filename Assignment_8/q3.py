# 3. Write a program to find sum of following series using functions :
# a. 1 + 2 + 3 + 4 + ..... + n
# b. 1! + 2! + 3! + 4! + ..... + n!
# c. 1^1 + 2^2 + 3^3 + ..... + n^n


def sum1(n):
    i = 1
    sum = 0

    while(i <= n):
        sum += i
        i += 1

    return sum


def sum2(n):
    i = 1
    sum = 0

    while(i <= n):
        mul = 1

        for j in range(1, i + 1):
            mul *= j

        sum += mul
        i += 1

    return sum


def sum3(n):
    i = 1
    sum = 0

    while(i <= n):
        sum += i ** i
        i += 1

    return sum


n = int(input("Enter the number : "))

res = sum1(n)
res2 = sum2(n)
res3 = sum3(n)

print("Sum of series a =", res)
print("Sum of series b =", res2)
print("Sum of series c =", res3)