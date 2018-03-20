# coding: cp949
x=1
y=1
z=1

print("x: "+str(x)+" y: "+str(y)+" z: {0}".format(z))  #z 를 출력할 수 있도록 포맷스트링으로 변경

if x or y:
    print("if x or y: 조건 만족")
else:
    print("if x or y: 조건 불만족")

if x and y:
    print("if x and y: 조건 만족")
else:
    print("if x and y: 조건 불만족")

if not x:
    print("not x 조건 만족")
else:
    print("not x 조건 불만족")

if not y:
    print("not y 조건 만족")
else :
    print("not y 조건 불만족")

if x and y and z:   #아래 조건이 만족할 수 있는 x,y,z값을 변경할 것
    print("x and y and z: 조건 만족")
else:
    print("x and y and z: 조건 불만족")

if x or y or z:
    print("x or y or z: 조건 만족")
else:
    print("x or y or z: 조건 불만족")




