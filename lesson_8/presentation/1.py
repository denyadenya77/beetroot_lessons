# Написать функцию, которая будет принимать температуру по цельсию и возвращать ее перевод в температуру по
# фаренгейту по формуле: (temp - 32) * (5/9)

def temp_f(a):
    c = a * 1.8 + 32
    return  c

user = int(input('Enter temp: '))

print(temp_f(user))