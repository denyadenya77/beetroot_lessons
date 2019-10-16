# В текстовый файл построчно записаны фамилия и имя учащихся класса и его оценка за контрольную.
# Вывести на экран всех учащихся, чья оценка меньше 3 баллов и посчитать средний балл по классу.
# Создать отдельные файлы по классам.

with open('klass.txt', 'r') as file_object:
    info = file_object.read()
    list1 = info.split('\n')
    list1.pop(-1)
    the_dict = {item : int(list1[index+1]) for index, item in enumerate(list1) if index % 2 == 0}
    print(the_dict)

for k, v in the_dict.items():
    if v < 3:
        print(k, ':', v)


middle_list = [v for k, v in the_dict.items()]
middle_int = sum(middle_list) / (len(middle_list) + 1)
result = (f'Средний балл: {middle_int}.')

with open('klass_1.txt', 'w') as file_object:
    for k, v in the_dict.items():
        if v < 3:
            string = f'{k} : {v}\n'
            file_object.write(string)
    file_object.write(result)