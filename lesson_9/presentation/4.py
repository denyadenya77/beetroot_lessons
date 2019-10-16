# Создать текстовый файл, записать в него построчно данные, которые вводит пользователь.
# Окончанием ввода пусть служит пустая строка.

start = open('user_input.txt', 'w')

while True:
    user = input('Enter: ')
    with open('user_input.txt', 'a') as file_object:
        file_object.write(user)
        file_object.write('\n')
    if user == '':
        break

