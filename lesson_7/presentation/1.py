# Подсчитать количество каждого элемента в списке. Результат в виде словаря.

l = [1, 2, 1, 4, 4, 5, 5]

dict = {}

for x in l:
    i = 1
    if x not in dict:
        dict[x] = i
    elif x in dict:
        dict[x] = i + 1

print(dict)
