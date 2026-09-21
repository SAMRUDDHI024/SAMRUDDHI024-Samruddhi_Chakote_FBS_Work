#8. Write a program to prompt user to enter userid and password. After verifying
#   userid and password display a 4 digit random number and ask user to enter the
#   same. If user enters the same number then show him success message otherwise
#   failed. (Something like captcha)

import random
uid = input('enter the userId : ')
pas = input('enter the password : ')

if(uid == 'sam@123' and pas == '12345'):
    cap = random.randint(1000,10000)
    print(f'captcha : {cap} ')
    user_cap =int(input('enter the captcha : '))
    if(cap == user_cap):
        print('Valid inputs , Sucessful login.')
    else:
        print('Incorrect captcha .')  
else:
    print('Invalid inputs.')