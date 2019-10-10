def game(t, time):
    if t >= 60 and t <= 90:
        print(print('у белок все по-кайфу'))
    elif time == 'summer' and ((t >= 60) and (t <= 100)):
        print('у белок все по-кайфу')
    else:
        print('у белок все очень плохо')

t = int(input())
time = input('if summer - print "summer"')

game(t, time)