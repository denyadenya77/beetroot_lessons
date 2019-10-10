import random

a = random.randint(0, 101)
print(a)

b = [1,2,3,4,5,6]
random.shuffle(b)
c = random.choice(b)
print(c)

d = random.random()
print(d)

e = random.uniform(0, 26)
print(e)