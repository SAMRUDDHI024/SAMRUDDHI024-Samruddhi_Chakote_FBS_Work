#7. Write a program to check if user has entered correct userid and password.
uid = input('enter the userId : ')
pas = input('enter the password : ')

if(uid == 'sam@123' and pas == '12345'):
    print('Valid inputs , Sucessful login.')
else:
    print('Invalid inputs.')