# coding: cp949

while True:
    sum=0
    num= int(input("시작하려면 1, 끝내려면 0 : "))
    if num ==1:
        x = int(input("X값을 입력하시오 : "))
        y = int(input("Y값을 입력하시오 : "))
        z = int(input("범위 Z를 입력하시오: "))
        for three in range(0,z,x):
            sum += three
        for five in range(0,z,y):
            sum += five

        print(sum)
    
    elif num==0:
        break

    else:
        continue

