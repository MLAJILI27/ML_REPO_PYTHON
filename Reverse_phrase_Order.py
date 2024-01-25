a = input('please enter a sentence: ')
b=a.split()
l=len(b)
for i in range(l-1,-1,-1):
    print(str(b[i]),end=' ')
