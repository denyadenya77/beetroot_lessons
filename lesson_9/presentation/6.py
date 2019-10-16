# Прочитать файл https://jsonplaceholder.typicode.com/todos, записать в новый файл все объекты с completed: true

import json

with open('todos.json') as file_object:
    info = json.load(file_object)

new_list = []

for x in info:
    for k, v in x.items():
        if k == 'completed' and v == True:
            new_list.append(x)

print(new_list)

with open('todos_true.jsom', 'w') as file_object:
    json.dump(new_list, file_object)