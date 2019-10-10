from datetime import date

def total_age(born_month, born_day, born_year):
    today = date.today()
    result = today.year - born_year - ((today.month, today.day) < (born_month, born_day))
    return result

burthday = list(map(int,input('Введите дату вашего рождения, например: 13 03 1997 ').split()))
name = input('Введите ваше имя: ')

born_day = burthday[0]
born_month = burthday[1]
born_year = burthday[2]

age = total_age(born_month, born_day, born_year)
print(f'Age for {name}: {age} years.')