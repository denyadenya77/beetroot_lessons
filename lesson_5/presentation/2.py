# Написать функцию, которая будет возвращать True если в списке, который передается функции как аргумент
# присутствует последовательность чисел 1, 2, 3, 4


def the_sum_2(s_list):
    c = {1, 2, 3, 4}
    if c.issubset(s_list):
        print(True)
    else:
        print(False)


s_list = [1, 2, 3, 4, 6, 8, 5]

the_sum_2(s_list)