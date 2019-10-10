import random

a = list()
b = list()


def add(one_list):
    t = 0
    while t < 10:
        one_list.append(random.randrange(1, 11))
        t = t + 1


add(a)
add(b)

print(a, b)

final = set(a).intersection(set(b))

if len(final) > 0:
    print(final)
else:
    print('no intersection')