'''
number = int(input('please enter a number: '))
x = list(range(1,int(number+1)))
a = []
for i in x :
    res = divmod(number,i)
    if res[1] == 0 :
        a.append(res[0])
        a.sort()
print(a)
'''

a= int(input('plese enter a number: '))
b= [i for i in range(1,a+1) if a % i == 0]
print(b)