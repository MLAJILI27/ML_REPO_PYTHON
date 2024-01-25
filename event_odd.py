number = int(input('please enter a number '))
res = divmod(number,2)
if res[1] == 0:
    print('pair')
else:
    print("impair")
