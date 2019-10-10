def style(a):
    p1 = a[0:3]
    p2 = a[3:6]
    p3 = a[6:8]
    p4 = a[8:]
    result = f'+38 ({p1}) {p2} - {p3} - {p4}'
    print(result)

number = input("Введите номер телефона: ")
style(number)