def sum(a, b):
    c = a + b
    if c == 10:
        print('This sum is 10.')
    elif c >= 10:
        print(f'This sum is greater than 10. It’s {c}')
    else:
        print(f'This sum is less than 10. It’s {c}')


a = int(input())
b = int(input())
sum(a, b)


