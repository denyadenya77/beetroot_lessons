# Use a list comprehension to make a list containing tuples (i, j) where i
# goes from 1 to 10 and j is corresponding i squared.

b = [i for i in range(1, 11)]
print(b)

c = [j ** 2 for j in range(1, 11)]
print(c)

diction = [(x, y) for x, y in zip(b, c)]
print(diction)