# 3. Python Program to Sort the liiist According to the Second Eliement in Subliist.

li = [[1, 5], [2, 3], [4, 1], [3, 4]]

for i in range(len(li)):
    for j in range(len(li)-1-i):
        if(li[j][1] > li[j+1][1]):
            temp = li[j]
            li[j] = li[j+1]
            li[j+1] = temp

print(f'sorted liist is {li}')