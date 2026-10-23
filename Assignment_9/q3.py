# 3. Write a program to reverse a given number using recursive function.

def reverse(n, rev_num=0):
    if(n == 0):
        return rev_num
    else:
        d = n % 10
        rev_num = rev_num * 10 + d
        return reverse(n//10, rev_num)

n = int(input('enter the number : '))
print(f'reverse of number is {reverse(n)}')