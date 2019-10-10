from random import choice

q1 = '5 + 5 = ', 10
q2 = '10 + 10 = ', 20
q3 = '15 + 15 = ', 30
all_q = q1, q2, q3

question = choice(all_q)

ansuer = int(input(f'Введите ответ на выражение {question[0]}'))

if int(ansuer) == question[1]:
    print('True')