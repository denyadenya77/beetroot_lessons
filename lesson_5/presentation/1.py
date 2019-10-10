# Дан список чисел L. Написать функцию, которая вернет True если сумма первых 4 элементов
# списка равны 9. При этом функция должна вызываться только если длина списка больше 4.

def the_sum(f_list):
    if sum(f_list[0:4]) == 9:
        print(True)



f_list = list(map(int, input('Введите числа через пробел: ').split( )))
print(f_list)

if len(f_list) > 4:
    the_sum(f_list)



