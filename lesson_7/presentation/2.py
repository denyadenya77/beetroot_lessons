# Вывести количество четных и нечетных елементов в рандомной последовательности.Результат в виде словаря.

dict = {}

even = 0
not_even = 0

for x in range(20):

    if x % 2:
        even += 1
        dict['even'] = even
    else:
        not_even += 1
        dict['not_even'] = not_even



print(dict)