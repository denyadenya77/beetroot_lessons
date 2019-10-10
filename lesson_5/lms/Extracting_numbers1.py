a = list(range(1, 101))

def func(item):
    if item % 7 == 0 and item % 5 != 0:
        return item


b = set(map(func, a))
b.remove(None)
f = sorted(b)

print(f)