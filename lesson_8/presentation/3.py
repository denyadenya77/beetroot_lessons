# Написать функцию которая принимает два аргумента: первый аргумент отвечает за выбор пользователя:
# минимум или максимум, второй аргумент - список элементов в котором нужно найти минимум или максимум.

def min1(a):
    c = sorted(a)
    result = c[0]
    return result

def max1(a):
    c = sorted(a)
    result = c[-1]
    return result

choise = {'min': min1, 'max': max1}

user = list(input('Enter operation and range: ').split())
print(user)

range1 = list(range(int(user[1]) + 1))
print(range1)

print(choise[user[0]](range1))