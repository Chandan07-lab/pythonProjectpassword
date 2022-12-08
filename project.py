import random as r
password_len=int(input('enter the length of password:'))
a='123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?'
if password_len>=12:
    random_num=r.choice(a[:9])
    random_lower=r.choice(a[9:35])
    random_upper=r.choice(a[35:61])
    random_symbol=r.choice(a[61:])
    temp=random_upper+random_num+random_lower+random_symbol
    for i in range(password_len-4):
        temp=temp+r.choice(a)
    print(temp,end='')
