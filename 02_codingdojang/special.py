# coding: cp949

list1 = [-1, 1, 3, -2, 2]
minus=[]
plus=[]

for i in list1:
    if i < 0:
        minus.append(i)
    else:
        plus.append(i)
print(minus+plus)
