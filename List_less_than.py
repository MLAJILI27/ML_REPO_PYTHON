a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89,1.2]
p = []
for i in a:
    if i < 5 :
        p.append(i)
print(p)
# with list comprehention
p2 = [i for i in a if i < 5 ]
print(p2)
