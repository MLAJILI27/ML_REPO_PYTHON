a = input('please enter a word: ')
l=len(a)
b=list(a)
c = b[::-1]
if b== c:
    print('palindrome')
else:
    print('not palindrome')