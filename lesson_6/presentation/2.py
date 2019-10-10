# Вывести количество четныx и нечетных елементов в рандомной последовательности.

# for
import random

l = list(random.sample(range(101), 50))
print(l)

one = 0
two = 0

for x in l:
    if x % 2:
        two += 1
    else:
        one += 1

print("Четных: " + str(one) + ". Нечетных: " + str(two))

# while

list1 = list(random.sample(range(101), 50))
print(list1)

one1 = 0
two1 = 0
i1 = 0

while i1 < len(list1):
    if list1[i1] % 2:
        two1 += 1
    else:
        one1 += 1
    i1 += 1

print("Четных: " + str(one1) + ". Нечетных: " + str(two1))