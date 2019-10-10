the_list = list(range(1, 101))

final = list()

for x in the_list:
    a = 0
    if x % 7 == 0 and x // 5 != a:
        final.append(x)

print(final)