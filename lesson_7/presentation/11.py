# Дан словарь со списком IP адресов у конкретного человека, например:
# {"Igor":['192.168.250.1', '192.168.250.2', '10.236.43.2'],"Denis":['xxx.xxx.xxx.xxx', 'yyy.yyy.yyy.yyy']}.
# Определить и вывести владельца по введенному IP адресу.


dict_of_ip = {"Igor":['192.168.250.1', '192.168.250.2', '10.236.43.2'],"Denis":['xxx.xxx.xxx.xxx', 'yyy.yyy.yyy.yyy']}
user = input('Enter: ')

for k, y in dict_of_ip.items():
    for x in y:
        if x == user:
            print(k)
