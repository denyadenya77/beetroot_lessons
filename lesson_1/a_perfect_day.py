from datetime import date
import calendar
my_date = date.today()

today = calendar.day_name[my_date.weekday()]
my_name = "Denys"

print('Good day ' + my_name + '! ' + today + ' is a perfect day to learn some python.')