# Посчитать количество 9 в списке.

# for
l = [1, 5, 9, 6, 9, 9]
a = 0

for x in l:
    if x == 9:
        a += 1

print(a)



# while

list1 = [1, 5, 9, 6, 9, 9]

b = 0

i = 0
while i < len(list1):
    if list1[i] == 9:
        b += 1
    i += 1


print(b)