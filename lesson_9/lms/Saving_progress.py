# Make a function that takes personal information as arguments, e.g., name,
# last name, phone number, address, etc. Then make another function that
# saves the data onto a file. Make sure that it works by checking that the
# file was created and that it contains the right data.

import json

def user(name, last_name, age, number, address):
    user_dict = {}
    user_dict.update({'name': name, 'last name': last_name, 'age': age, 'number': number, 'address': address})
    return user_dict

def saving(the_dict):
    with open('user_info.json', 'w') as file_object:
        json.dump(the_dict, file_object)


name = input('Enter your name: ')
last_name = input('Enter your last name: ')
age = input('Enter your age: ')
number = input('Enter your phone number: ')
address = input('Enter your address: ')

the_dict = user(name, last_name, age, number, address)
saving(the_dict)
