


while(True):
    age= (input("나이를 입력하세요(종료하려면 종료를 입력하세요) :"))
    if(age<'3'):
        print("입장권 무료입니다")
    elif('3'<=age<='12'):
        print("입장권  가격은 10달러입니다")
    elif(age=='종료'):
        break
    else:
        print("입장권 가격은 15달러입니다")