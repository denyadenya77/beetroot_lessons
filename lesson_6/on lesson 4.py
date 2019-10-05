# Написать функцию, которая будет принимать пароль. Если в пароле есть буквы и цифры и его длина не менее 10
# символов вывести: “Your password is strong.” в противном случае “Your password is not strong enough.”

# for

def enter(a):
    b = list()
    if len(a) >= 10:
        for x in a:
            if x is int or x is str:
                b.append(1)
    if sum(b) == len(b):
        print("Your password is strong.")
    else:
        print("Your password is not strong enough.")


password = list(input('Enter your password: '))

enter(password)

# while

def enter_2(a):
    b = list()
    if len(a) >= 10:
        i = 0
        while i < len(a):
            for a[i] in a:
                if a[i] is int or a[i] is str:
                    b.append(1)
            i += 1
    if sum(b) == len(b):
        print("Your password is strong.")
    else:
        print("Your password is not strong enough.")

enter_2(password)


