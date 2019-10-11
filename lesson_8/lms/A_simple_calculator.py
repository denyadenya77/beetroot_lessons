# Create a function called make_operation, which takes in a simple
# arithmetic operator as a first parameter (to keep things simple let it
# only be ‘+’, ‘-’ or ‘*’) and an arbitrary number of arguments (only
# numbers) as second parameter. Then return the sum or product of all the
# numbers in the arbitrary parameter.

def make_operation(operator, *args):
    print(args)
    result = 0
    if operator == '-':
        for x in args:
            result = args[0] - sum(args[1:])
    if operator == '+':
        result = sum(args)
    if operator == '*':
        result = args[0]
        for i, x in enumerate(args):
            if i < (len(args) - 1):
                result = result * args[i + 1]
    return result

print(make_operation('+', 7, 7, 2))
print(make_operation('-', 5, 5, -10, -20))
print(make_operation('*', 7, 6))