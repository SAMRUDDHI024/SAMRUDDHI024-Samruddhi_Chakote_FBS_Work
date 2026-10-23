# 1 2 3 4 5 
# 2       5 
# 3     5   
# 4   5     
# 5      


n = 5

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i == 1:
            print(j, end=" ")
        elif j == 1 and i <= 5:
            print(i, end=" ")
        elif j == n - i + 2 and i < 5:
            print(5, end=" ")
        else:
            print(" ", end=" ")
    print()