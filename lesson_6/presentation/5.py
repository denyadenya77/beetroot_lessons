# Посчитать факториал для введенного пользователем числа.

user = int(input('Enter: '))

fact = 1
while user > 1:
    fact *= user
    user -= 1

print(fact)

# for

user1 = int(input('Enter: '))
fact1 = 1

for i in range(2, user1 + 1):
    fact1 *= i

print(fact1)