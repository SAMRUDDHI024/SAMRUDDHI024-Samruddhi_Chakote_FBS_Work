#      1
#    1   2
#   1     3
#  1       4
# 1  2  3  4  5


n = 5

for i in range(1, n + 1):
    print(" " * (n - i), end="")

    if i == 1:
        print(1)
    elif i == n:
        print(" ".join(str(j) for j in range(1, n + 1)))
    else:
        print(1, " " * (2 * i - 3), i)