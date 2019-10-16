# Посчитать количество строк в файле и количество слов и символов в каждой строке https://ru.lipsum.com/feed/html

import os

file_address = os.path.abspath(os.path.join(os.path.dirname(__file__), 'Lorem_Ipsum.txt'))

with open(file_address, 'r') as file_object:
    text = file_object.read()
    n = text.count('\n') # кол-во строк
    print(f'Колличество строк: {n}')

list_of_str = text.split('\n') # возвращает список строк
list_of_str.pop()
print(list_of_str)


the_dict = {}
i = 0

for x in list_of_str:

    # находит все пустые строки в списке
#     if x == '':
#         i += 1
# print(i)

    # обрабатывает первую пустую строку - послед. игнор.
    # k = list_of_str.index(x) + 1
    # v = x
    # the_dict.update({k: v})



    # обрабатывает первую пустую строку - послед. игнор.
    # if len(x) > 0:
    #     k = list_of_str.index(x) + 1
    #     v = len(x)
    #     the_dict.update({k: v})
    # elif len(x) == 0:
    #     k = list_of_str.index(x) + 1
    #     v = None
    #     the_dict.update({k: v})

print(the_dict)

