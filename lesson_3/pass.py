def enter(your_pass):
    abc = len(your_pass)
    if abc >= 10:
        print('Your password is strong.')
    else:
        print('Your password is not strong enough.')


your_pass = input('Enter your pass: ')
enter(your_pass)