# необходимо объединить два прайс-листа (задаются в виде словарей) с тем условием, что если наименование
# товара присутствует в обоих прайсах, то в итоговый прайс помещается тот, чья цена выше.
# (с помощью списковых включений)

price_list_1 = {'apple': 2, 'mango': 3, 'vodka': 6}
price_list_2 = {'vodka': 9, 'mango': 4, 'apple': 1}

# price_list_3 = {______ for k, v in price_list_1.items() for i, j in price_list_2.items() if k == i and v > j if k == i and j > v}


price_list_3 = {k:v for k,v in price_list_1.items() for i,j in price_list_2.items() if k == i and v > j}
print(price_list_3)
price_list_4 = {i:j for k,v in price_list_1.items() for i,j in price_list_2.items() if k == i and j > v}
print(price_list_4)
price_list_3.update(price_list_4)
print(price_list_3)

# for k, v in price_list_1.items():
#     for i, j in price_list_2.items():
#         if k == i and v > j:
#             price_list_3.update({k: v})
#         if k == i and j > v:
#             price_list_3.update({i: j})
#
# print(price_list_3)