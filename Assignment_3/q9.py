#9. Input 5 subject marks from user and display grade(eg.First class,Second class ..)

m1 = int(input('enter the marks of subject 1 : '))
m2 = int(input('enter the marks of subject 2 : '))
m3 = int(input('enter the marks of subject 3 : '))
m4 = int(input('enter the marks of subject 4 : '))
m5 = int(input('enter the marks of subject 5 : '))

avg =(m1 + m2 + m3 + m4 + m5) / 500
p = avg * 100

if(p > 80):
    print(f'with percentage {p} % the grade is First class .')
elif(p > 60):
    print(f'with percentage {p} % the grade is Second class .')
elif(p >= 40):
    print(f'with percentage {p} % the grade is Pass.')
else:
    print(f'with percentage {p} % the grade is failed .')