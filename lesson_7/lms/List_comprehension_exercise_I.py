# Consider the following list: a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100].
# Now, make a program (no longer than one line) that makes a new list
# containing all the values in a
# but no even numbers.

a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
b = [i for i in a if i % 2 == 0]
print(b)