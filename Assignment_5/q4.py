#4. WAP to print Armstrong number within a given range

start = int(input("Enter starting number: "))
end = int(input("Enter ending number: "))

for n in range(start, end + 1):

    temp = n
    count = 0

   
    while temp > 0:
        count = count + 1
        temp = temp // 10

    temp = n
    sum = 0
    while temp > 0:
        d = temp % 10
        sum = sum + d ** count
        temp = temp // 10

    if sum == n:
        print(n)