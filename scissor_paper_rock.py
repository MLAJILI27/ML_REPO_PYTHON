import random
import math
'''
program for rock paper game
'''

l_choice = ['scissors', 'paper', 'rock']
def player_ch():
    flag = False
    print("0: scissors")
    print("1: paper")
    print("2: rock")
    while flag == False:
        pl_choice = input('please entre a choice: ')
        if (pl_choice == str(0) ):
            flag = True
            print('player choice',l_choice[0])
        elif (pl_choice == str(1)):
            flag = True
            print('player choice',l_choice[1])
        elif (pl_choice == str(2 ) ):
            flag = True
            print('player choice',l_choice[2])
        else:
            print('not correct')
            flag = False
    return l_choice[int(pl_choice)]
def comp_ch():
    i = random.randint(0, len(l_choice)-1)
    print('computer choice', l_choice[i])
    return l_choice[i]

def compare():
    score = {'p_score': 0, 'c_score': 0}
    for i in range (1,4):
        print('-------round------- :'+ str(i))
        a=player_ch()
        b=comp_ch()
        if a == 'rock' and b == 'scissors' or a == 'paper' and b == 'rock' or a == 'scissors' and b == 'paper':
            score['p_score'] = score['p_score'] + 1
            print('computer score: ' + str(score['c_score']) + '\t' + 'player score : ' + str(score['p_score']))
        elif a == 'scissors' and b == 'rock' or a == 'rock' and b == 'paper' or a == 'paper' and b == 'scissors':
            score['c_score'] = score['c_score'] + 1
            print('computer score: '+ str(score['c_score'])  + '\t' + 'player score : ' + str(score['p_score']) )
        elif a == b:
            print('equal score for both side ' + 'computer score: ' + str(score['c_score']) + '\t' + 'player score : ' + str(score['p_score']))
        else:
            print('not correct')

if __name__ == '__main__':
    compare()