n=input('please enter a number: ')
x= int(n)
print(x)

for i in range(0,x):
    c= (i*2)+1
    print(' '*x+'*'*c+' '*x)
    x= x-1