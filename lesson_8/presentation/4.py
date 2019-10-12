# Написать функцию пересечения и функцию объединения неограниченного количества последовательностей.

import random

def cross_and_combine(a):
    cross_subset = set(a[0])
    combite_list = a[0]
    i = 1
    #cross
    while i < len(a):
        cross_subset = cross_subset.intersection(set(a[i]))
        # combine
        combite_list = combite_list + a[i]
        i += 1



    return cross_subset, sorted(combite_list)


# ввод количества последовательностей
user = int(input('Enter: '))

# создаем кол-во последовательностей
list_of_lists = [random.sample(range(50), 25) for x in range(user)]
print(list_of_lists)

print(cross_and_combine(list_of_lists))

