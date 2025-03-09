import random

chars = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOOOOPASDFGHJKLZXCVBNM1234567890!@#$%^&*№?*'
symbols = ''
lenght = int(input('Какой длинны будет ваш пароль?'))
for i in range(lenght):
    symbols += random.choice(chars)
    
print(symbols)
