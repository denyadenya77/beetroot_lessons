# Вам дан словарь, состоящий из пар слов. {“Hello”: “Hi”, “Bye”: “Goodbye”, “List”: “Array”}
# Каждое слово является синонимом к парному ему слову. Все слова в словаре различны.
# Определить синоним для слова введенного пользователем.

dict = {'Hello': 'Hi', 'Bye': 'Goodbye', 'List': 'Array'}

user = input('Enter: ').title()

if user in dict:
    print(dict[user])
else:
    for k, v in dict.items():
        if v == user:
            print(k)