# Попросить пользователя ввести информацию про членов его семьи записывая их имя и возраст в
# отдельные словари списка. Вывести имя самого пожилого человека в семье.

list_of_dicts = [{}, {}]
key = 1

# добавляем имена и возраст в словари
while True:
    user = list(input('Enter: ').split())
    print(user)
    if user[0] != 'q':
        list_of_dicts[0].update({key: user[0]})
        list_of_dicts[1].update({key: user[1]})
        key += 1
    else:
        break

# вычисляем наибольший возраст
ages = list(list_of_dicts[1].values())
max_age = max(ages)

# ищем ключ к возрасту
max_age_key_name = 0
for k, v in list_of_dicts[1].items():
    if v == max_age:
        max_age_key_name = k

# ищем имя по ключу
for k, v in list_of_dicts[0].items():
    if k == max_age_key_name:
        print(f'The oldest member of your family is {v}: {max_age} years.')


