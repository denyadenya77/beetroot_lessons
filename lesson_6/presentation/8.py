# Вывести последовательность Фибоначчи где количество элементов последовательности задается пользователем.

user = int(input('Enter: '))
fib = [1, 1]

while len(fib) < user:
    fib.append(fib[-2] + fib[-1])

print(fib)
