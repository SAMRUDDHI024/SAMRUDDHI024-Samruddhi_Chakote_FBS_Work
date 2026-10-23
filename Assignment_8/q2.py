#2. Write a program to calculate area of circle


def calArea(redius):
    area = 3.14 * redius * redius
    return area


r = int(input('enter the redius : '))
res = calArea(r)
print(f'Area of rectangle : {res}')