#5. Write a program to check whether the triangle is equilateral, isosceles or scalene
#   triangle.

s1 = int(input('enter the length of side 1 of triangle : '))
s2 = int(input('enter the length of side 2 of triangle : '))
s3 = int(input('enter the length of side 3 of triangle : '))

if(s1 == s2 and s2 == s3 ):
    print('Triangle is an equilateral Triangle .')
elif(s1==s2 or s2==s3 or s1==s3):
    print('Triangle is an isosceles Triangle .')
else:
    print('Triangle is an scalene Triangle .')  # if add condition then (s1!=s2 or s2!=s3 or s1!=s3)