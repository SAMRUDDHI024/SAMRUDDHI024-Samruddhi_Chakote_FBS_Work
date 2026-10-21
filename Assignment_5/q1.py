#1. Write a program to prompt user to enter userid and password. If Id and
# password is incorrect give him chance to re-enter the credentials. Let him try 3
# times. After that program to terminate. 


for i in range(1,4):
    uid = input('enter the userId : ')
    pas = input('enter the password : ')

    if(uid == 'sam@123' and pas == '12345'):
       print('Valid inputs , Sucessful login.')
       break
    else:
       print('Invalid inputs.')
else :
  print('your 3 attempt are over ')
