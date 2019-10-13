# Написать функцию для подсчета периметра фигуры в зависимости от того какую фигуру укажет пользователь.

user = list(map(int, input('Enter side length: ').split()))

perimeter = lambda x: sum(x)

print(perimeter(user))