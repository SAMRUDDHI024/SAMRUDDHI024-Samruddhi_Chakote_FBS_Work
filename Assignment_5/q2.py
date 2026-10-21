#2. Enter number of students from user. For those many students accept marks of 5
# subject marks from user and calculate percentage. Display all percentage and
# average percentage of students

n = int(input("Enter number of students: "))

tp = 0

for i in range(1, n + 1):
    tm = 0

    print("Enter marks for Student", i)

    for j in range(1, 6):
        m = int(input("Enter marks of subject : "))
        tm = tm + m

    p = tm / 5
    print(f'percentage i=od student {i} is : {p}')

    tp = tp + p

avg_percentage = tp / n

print(f'Average Percentage {avg_percentage} % ')