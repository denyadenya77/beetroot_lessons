# Написать функцию, которая будет принимать пароль. Если в пароле есть 1 большая буква и хотя бы 5 цифр, и его длина
# не менее 10 символов вывести: “Your password is strong.” в противном случае “Your password is not strong enough.”

password = list(input('Enter your password: '))

def enter(a):
    control = None
    control_int = list()
    if len(a) >= 10:
        for x in a:
            if x.isupper():
                control = True
            elif x.isdigit():
                control_int.append(1)
    if (control == True) and (len(control_int) >= 5):
        print('Your password is strong.')
    else:
        print('Your password is not strong enough.')

enter(password)

# while

def enter1(a):
    control = None
    control_int = list()
    if len(a) >= 10:
        i = 0
        while i < len(a):
            if a[i].isupper():
                control = True
            elif a[i].isdigit():
                control_int.append(1)
            i += 1
    if (control == True) and (len(control_int) >= 5):
        print('Your password is strong.')
    else:
        print('Your password is not strong enough.')

enter1(password)