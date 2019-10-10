# Вывести последовательность Коллатца для числа введенного пользователем. Остановится когда число достигнет 1.

user = list(map(int, input('Enter: ')))
l = [user]

while user[-1] != 1:
    if user[-1] % 2 == 0:
        l.append(user[-1] / 2)
    else:
        l.append(user[-1] * user[-1] + 1)

print(user) # код не выводит последовательность
