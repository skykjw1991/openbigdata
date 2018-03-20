# coding: cp949

print("마름모 출력 프로그램 ver2.0")

star = int(input("홀수를 입력하세요(0 <- 종료): "))
while True:
    if star%2 !=0:
        for i in range(1, int(star/2)+1):
            print(" "*(int(star/2)-i+1) + "*"*(2*i-1))
        for j in range(int(star/2)+1,0,-1):
            print(" "*(int(star/2)-j+1) + "*"*(2*j-1))
        break
    else:
        break
