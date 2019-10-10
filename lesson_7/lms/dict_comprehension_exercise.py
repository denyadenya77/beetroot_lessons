# Make a program that given a whole sentence will make a dict containing all unique words as keys and
# the number of occurrences as values.

a = 'Make a program that given a whole sentence will make a dict containing all unique words as keys and ' \
    'the number of occurrences as values.'

a.replace('.', '')
list = a.split()
print(list)

dict = {}


for x in list:
  dict[x] = list.index(x)

print(dict)