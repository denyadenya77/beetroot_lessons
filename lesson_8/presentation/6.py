# Написать функцию, которая принимает строку как аргумент и возвращает ее в обратном порядке не
# используя функцию reversed или срезы.

def reversed1(user):
    list1 = []
    for x in user:
        list1.insert(0, x)
    a = ''
    print(a.join(list1))


user = input('Enter: ')
print(user)

reversed1(user)