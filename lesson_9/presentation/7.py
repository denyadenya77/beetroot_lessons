# Посчитать количество повторяющихся слов в первом абзаце https://ru.lipsum.com/feed/html из файла.

with open('txt_lorem.txt', 'r') as file_obj:
    info = file_obj.read()

info = info.replace('.', '')
info = info.replace(',', '')
info = info.lower()

list_info = info.split(' ')

new_dict = {}
for x in list_info:
    i = 0      #value
    name = x   #key
    for j in list_info:
        if name == j:
            i += 1
    if i > 1:
        new_dict.update({name: i})

for k in sorted(new_dict.keys()):
    print (k, ':', new_dict[k])
