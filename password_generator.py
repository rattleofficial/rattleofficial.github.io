import random

while True:
    password='ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789abcdefghijklmnopqrstuvwxyz!@#$%&*'
    b=int(input('Enter how many characters is necessary for your password:'))
    a="".join(random.sample(password,b))
    print(a)

