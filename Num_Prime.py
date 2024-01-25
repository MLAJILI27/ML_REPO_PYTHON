def get_number():
    return int(input('Please enter a number: '))
def prime(x):
    if x % x == 0 and x % 1 == 0 :
        if x !=2 and x % 2 != 0:
            print('prime')
        elif  x == 2 or x==1:
            print('prime')
        else:
            print('not prime')
if __name__ == '__main__':

    x= get_number()
    prime(x)