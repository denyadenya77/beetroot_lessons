# Создать файл nums.txt с рандомными цифрами и нужно среди них найти самую большую цифру
# и написать его уже в новый max_num.txt файл

import random, os

with open('nums.txt', 'w') as file_object:
    ints = random.sample(range(100), 5)
    ints_str = ', '.join(map(str, ints))
    file_object.write(ints_str)

file_address = os.path.abspath(os.path.join(os.path.dirname(__file__), 'nums.txt'))

with open(file_address, 'r') as file_object:
    nums = file_object.read()
    nums_1 = map(int, nums.split(', '))
    max_int = max(nums_1)

with open('max_num.txt', 'w') as file_object:
    file_object.write(str(max_int))

with open('max_num.txt', 'r') as file_object:
    print(file_object.read())