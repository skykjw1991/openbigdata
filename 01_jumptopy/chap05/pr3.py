
while(True):
    num = int(input("양수를 입력하세요(종료 -1): "))
    if(num == -1):
        break
    elif(num<-1):
        print("양수를 입력하세요")
    elif(num%10 == 0 ):
        print("10의 배수입니다")
    else:
        print("10의 배수가 아닙니다")

