# С помощью random сгенерировать 2 целых числа и спросить у пользователя ответ суммы этих чисел.
# Если пользователь посчитал верно то засчитать ему одно очко. Повторять пока пользователь не введет ‘q’.

from random import randint

points = 0

while True:
    a = randint(0, 11)
    b = randint(0, 11)
    user = input(f'Enter the sum of {a} and {b}: ')

    if user == 'q':
        print(points)
        break
    elif a + b == int(user):
        points += 1
        print(f'Right! Points = {points}')
    elif a + b != int(user):
        print('Wrong!')

