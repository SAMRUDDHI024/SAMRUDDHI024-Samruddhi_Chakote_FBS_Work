#2. Write a program to input any alphabet and check whether it is vowel or consonant.

a =input('enter the alphabet : ')

if(a == 'a' or a == 'e' or a == 'i' or a == 'o' or a == 'u' or a == 'A' or a == 'E' or a == 'I' or a == 'O' or a == 'U' ):
    print(f'{a} is Vowel .')
else:
    print(f'{a} is Consonanat .')