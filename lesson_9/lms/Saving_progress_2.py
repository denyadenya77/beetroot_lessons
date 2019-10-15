# Add to the previous program a function for opening up the same file which the data was saved on.
# Make sure that it works by making the function print out the data.

import json

with open('user_info.json') as file_object:
    user_info_dict = json.load(file_object)

for k, v in user_info_dict.items():
    print(k, ':', v)