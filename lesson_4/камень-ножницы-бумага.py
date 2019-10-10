import random

s = ['rock', 'scissors', 'paper']
i = input("Enter your choise: ")

def game(s, i):
    opp = random.choice(s)
    if opp == i:
        print('try again')
    elif (opp == 'rock' and i == 'scissors') or (opp == 'scissors' and i == 'paper') or \
            (opp == 'papre' and i == 'rock') or (opp == 'paper' and i == 'rock'):
        print(opp)
        print('you lose')
    else:
        print(opp)
        print('you won')

game(s, i)