from random import randint

a = randint(0, 10)
user = int(input('Choose the number: '))

while (1 == 1):

    if a < user:
        user = int(input('The number is <. Choose again: '))
    elif a > user:
        user = int(input('The number is >. Choose again: '))
    elif a == user:
        print('Right!')
        break
    else:
        continue

