# Пользователь должен ввести последовательность чисел через пробел.Для каждого числа выведите слово YES
# (в отдельной строке), если это число ранее встречалось в последовательности или NO, если не встречалось.

user = list(map(int, input('Enter: ').split()))
print(user)

in_set = set()


for x in user:
    if x not in in_set:
        print(x)
        print('no')
        in_set.add(x)

    elif x in in_set:
        print(x)
        print('yes')


print(in_set)

# while

print(user)

in_set1 = set()

ii = 0
while ii < len(user):
    if user[ii] not in in_set1:
        print(user[ii])
        print('no')
        in_set1.add(user[ii])

    elif user[ii] in in_set1:
        print(user[ii])
        print('yes')
    ii += 1

print(in_set1)