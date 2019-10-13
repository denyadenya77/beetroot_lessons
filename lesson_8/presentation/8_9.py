import random

# 8. Написать функцию, которая генерирует матрицу размером n*n с рандомными числами. Размер указывает пользователь.

user = int(input('Enter: '))

list_of_lists = [random.sample(range(25), user) for x in range(user)]

for x in list_of_lists:
    print(x)


# 9. Используя матрицу из прошлого примера, написать функцию, которая вернет номер ряда с максимальной суммой элементов.

def max_list_sum(a):
    result = 0
    i = None
    ii = []
    for x in a:
        if sum(x) > result:
            result = sum(x)
            i = list_of_lists.index(x) + 1
    for x in a:
        if sum(x) == result:
          ii.append(list_of_lists.index(x) + 1)
    return result, i, ii

c = max_list_sum(list_of_lists)[2]

if len(c) > 1:
    print(f'Max sum is {max_list_sum(list_of_lists)[0]} on a {max_list_sum(list_of_lists)[1]} '
          f'and {max_list_sum(list_of_lists)[2][0:]} lines')
else:
    print(f'Max sum is {max_list_sum(list_of_lists)[0]} on a {max_list_sum(list_of_lists)[1]} line.')