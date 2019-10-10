def game(t, time):
    if (t in range(60, 91)) or (time == 'summer' and t in range(60, 101)):
        print('у белок все по-кайфу')
    else:
        print('у белок все очень плохо')

t = int(input())
time = input('if summer - print "summer"')

game(t, time)