# Написать функцию поиска минимума в произвольном количестве элементов переданных в функцию/

import random

def min_max_int(a):
    c = sorted(a)
    int_min = c[0]
    int_max = c[-1]
    print(c)
    return int_min, int_max


list_1 = list(random.sample(range(50), 25))

result = min_max_int(list_1)
print(f'Min = {result[0]}, max = {result[1]}')