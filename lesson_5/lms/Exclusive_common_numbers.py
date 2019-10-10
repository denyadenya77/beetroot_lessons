import random

a = list()
b = list()


def add(one_list):
    if True:
        one_list.append(random.randrange(1, 11))
        one_list.append(random.randrange(1, 11))
        one_list.append(random.randrange(1, 11))
        one_list.append(random.randrange(1, 11))
        one_list.append(random.randrange(1, 11))
        one_list.append(random.randrange(1, 11))
        one_list.append(random.randrange(1, 11))
        one_list.append(random.randrange(1, 11))
        one_list.append(random.randrange(1, 11))
        one_list.append(random.randrange(1, 11))

add(a)
add(b)

print(a, b)

final = set(a).intersection(set(b))

if len(final) > 0:
    print(final)
else:
    print('no intersection')