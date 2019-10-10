# Генерируется квадратная матрица (с помощью списковых включений). Найти сумма элементов
# ее главной и побочной диагоналей.

matrix = [[x for x in range(5)] for x in range(5)]
print(matrix)


main = 0
side = 0
for x in range(len(matrix)):
    main = main + matrix[x][x]
    side = side + matrix[x][(len(matrix) - 1) - x]

print(main, side)