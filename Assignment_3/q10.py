#10. Write a program to check if person is eligible to marry or not (male age >=21 and
#    female age>=18)

gender = input('enter the gender as ( M / F ) : ')
age = int(input('enter the age : '))

if(gender == 'F'):
    if(age >= 18):
        print('Girl is eligible to marriage')
    else:
        print('Girl is  not eligible to marriage')
else:
    if(age >= 21):
        print('Boy is eligible to marriage')
    else:
        print('Boy is  not eligible to marriage')