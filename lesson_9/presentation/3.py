# Посчитать количество строк в файле и количество слов и символов в каждой строке https://ru.lipsum.com/feed/html

import os

file_address = os.path.abspath(os.path.join(os.path.dirname(__file__), 'Lorem_Ipsum.txt'))

with open(file_address, 'r') as file_object:
    text = file_object.read()
    n = text.count('\n') # кол-во строк
    print(f'Колличество строк: {n}')

list_of_str = text.split('\n') # возвращает список строк
list_of_str.pop()


the_dict = {}

for index, x in enumerate(list_of_str, 1):
    if len(x) > 0:
        k = index
        v = len(x)
        the_dict.update({k: v})
    elif len(x) == 0:
        k = index
        v = None
        the_dict.update({k: v})

print(the_dict)

