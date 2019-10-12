# Имитировать работу функции print(*args, sep=’’, end=’\n’) используя поток вывода sys.stdout.write(text)

import sys

def no_print(sep, end, *args):
    result_str = None
    for x in args:
        result_str = sep.join(x)
    sys.stdout.write(result_str + end)


user = list(input('Enter sep, end, args: ').split())
print(user)

no_print(user[0], user[1], user[2:])