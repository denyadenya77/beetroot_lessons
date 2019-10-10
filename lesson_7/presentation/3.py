# Для каждого слова из данного текста https://ru.lipsum.com/feed/html подсчитайте, сколько раз оно встречалось
# в этом тексте ранее. Результат в виде словаря.

user = input('Enter: ')
user = user.lower()
user = user.replace('.', '')
user = user.replace(',', '')
print(user)

list = user.split()
print(list)

dict = {}

for x in list:
    i = 1
    if x not in dict:
        dict[x] = i
    elif x in dict:
        dict[x] = i + 1

print(dict)