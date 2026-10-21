#    1 
#   1 1 
#  1 2 1 
# 1 3 3 1 


for i in range(1, 5):
    print(" " * (4 - i), end="")

    for j in range(1, i + 1):
        if j == 1 or j == i:
            print(1, end=" ")
        elif ( i == 3):
            print(2, end=" ")
        else :
            print(3, end=" ")

        

    print()