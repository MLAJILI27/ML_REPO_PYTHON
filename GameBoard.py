import string
'''
Definition : Build a game board like this example :
--- --- ---
| 1 | 2 | 3 |
--- --- ---
| 4 | 5 | 6 |
--- --- ---
| 7 | 8 | 9 |
--- --- ---
'''
def treV():
    for i in range(1,10):
        for j in range(1,4):
            break
        if i == 3 or i == 6:
            print('| ' + str(i)+ ' |')
            print('--- ' * 3 )
        else:
            print('| '+ str(i), end=' ')
    print('|')
def treH():
    for i in range(0,1):
     print('--- ' * 3 )
if __name__ == '__main__':
    treH()
    treV()
    print('--- ' * 3)



