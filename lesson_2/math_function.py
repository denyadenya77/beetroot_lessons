def count(a, c, b, d, f):
    r = (a**c - b + d) // f
    b = (a ** c - b + d) % f
    return r, b

r = count(15, 2, 20, 5.5, 6)

print(r)