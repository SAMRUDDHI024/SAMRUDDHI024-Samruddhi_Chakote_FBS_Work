# 1         
# 1 2       
# 1   3     
# 1     4   
# 1 2 3 4 5 



n = 5

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if j == 1 or j == i or i == n:
            if j <= i:
                print(j, end=" ")
            elif i != n:
                print(" ", end=" ")
        else:
            print(" ", end=" ")
    print()