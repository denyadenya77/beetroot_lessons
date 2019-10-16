# Создайте файл nums.txt, содержащий несколько чисел, записанных через пробел. Напишите программу,
# которая подсчитывает и выводит на экран общую сумму чисел, хранящихся в этом файле.

import random, os

with open('nums1.txt', 'w') as file_object:
    ints = random.sample(range(100), 5)
    ints_str = ' '.join(map(str, ints))
    print(ints_str)
    file_object.write(ints_str)

with open('nums1.txt', 'r') as file_object:
    nums = file_object.read()
    nums_1 = map(int, nums.split(' '))
    the_sum = sum(nums_1)
    print(the_sum)