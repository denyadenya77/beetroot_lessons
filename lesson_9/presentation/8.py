# Создать два файла .json из https://jsonplaceholder.typicode.com/todos в одном файле содержится id и title,
# в другом файле - id и completed. В результирующий файл записать JSON: {"id": 56, "title": "", "completed": true}

import json

with open('todos.json') as file_obj:
    info = json.load(file_obj)

with open('todos_id_and_title.json', 'w') as file_obj:
    id_title_list = []
    for x in info:
        in_dict = {}
        for k, v in x.items():
            if k == 'id':
                in_dict[k] = v
            elif k == 'title':
                in_dict[k] = v
        id_title_list.append(in_dict)
    json.dump(id_title_list, file_obj)

with open('todos_id_and_comp.json', 'w') as file_obj:
    id_comp_list = []
    for x in info:
        in_dict_1 = {}
        for k, v in x.items():
            if k == 'id':
                in_dict_1[k] = v
            elif k == 'completed':
                in_dict_1[k] = v
        id_comp_list.append(in_dict_1)
    json.dump(id_comp_list, file_obj)

with open('todos_result.json', 'w') as file_obj:
    result_list = id_title_list[:]
    list1 = []
    for x in id_comp_list:
        for k, v in x.items():
            if k == 'completed':
                list1.append(v)
    i = 0
    while i < len(info):
        for x in result_list:
            x['completed'] = list1[i]
            i += 1
    json.dump(result_list, file_obj)