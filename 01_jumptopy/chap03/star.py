# coding: cp949

print("마름모 출력 프로그램 ver1.0")

star = int(input("홀수를 입력하세요(0 <- 종료): "))
while True:
    if star%2 !=0:
        for i in range(1, star+1):
            print(" "*(star-i) + "*"*(2*i-1))
        break
    else:
        break

