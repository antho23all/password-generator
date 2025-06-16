# Password Generator



import random

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@£$%^&*().,?0123456789'


number = input('number of passwords?')
number = int(number)

length = input('password length?')
length = int(length)


for p in range(1):
    password = ''
    for c in range(20):
        password += random.choice(chars)
    print(password)
