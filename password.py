import random

print('Your password is: ')

chars = 'abcdefghijklmnopqrstuvwxysABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()?'

password = ''
for x in range(20):
    password += random.choice(chars)

print(password)
