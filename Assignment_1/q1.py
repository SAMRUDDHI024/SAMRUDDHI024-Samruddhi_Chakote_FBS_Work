#1. Write a program to calculate the percentage of student based on marks of any 5 subjects.


#take input 

m1 = int(input('enter marks of subject 1 :'))
m2 = int(input('enter marks of subject 2 :'))
m3 = int(input('enter marks of subject 3 :'))
m4 = int(input('enter marks of subject 4 :'))
m5 = int(input('enter marks of subject 5 :'))

#Perform opration

# percentage = ((m1 + m2 + m3 + m4 + m5)/500)*100
avg =(m1+m2+m3+m4+m5)/500
percentage = avg * 100


#Display result
print(f'percentage of marks m1:{m1}, m2:{m2}, m3:{m3}, m4:{m4}, m5:{m5} is {percentage}% .')

