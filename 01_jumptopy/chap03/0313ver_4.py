# coding: cp949

money =0
grade =0
age=int(input("나이를 입력하세요 : "))

if 0 <= age <= 3:
    money=0
    grade="유아"
elif 4 <= age <= 13:
    money=2000
    grade="어린이"
elif 14<= age <= 18:
    money=3000
    grade="청소년"
elif 19<=age<=65:
    money=5000
    grade="성인"
elif 66 <= age:
    money=0
    grade="노인"
else:
    print("다시입력하세요")

print("귀하는 %s 등급이며, 요금은 %d 원 입니다" %(grade, money))

if 4<=age<=65:
    pay_type=int(input("요금 유형을 선택하세요. (1:현금 2: 공원 전용 신용 카드) : "))
    if pay_type==1:
        if 4<=age<=65:
            pay=int(input("요금을 입력하세요 : "))
            if money > pay:
                print("%d가 모자랍니다. 입력하신 %d를 반환합니다" %(-(pay-money), pay))
            elif money == pay:
                print("감사합니다. 티켓을 발행합니다.")
            else :
                print("감사합니다. 티켓을 발행하고 거스름돈 %d를 반환합니다" %(-(money-pay)))
        else :
            print("감사합니다. 티켓을 발행합니다.")

    elif pay_type==2:
        print("결제금액의 10% 할인, 60~65세 장년은 추가 5% 할인")
        if 60<=age<=65:
            print("%d원 결제 되었습니다. 티켓을 발행합니다." %(money*0.90*0.95))
        else:
            print("%d원 결제 되었습니다. 티켓을 발행합니다." %(money*0.90))

    else:
        print("다시 선택하세요")
else:
    print("감사합니다. 티켓을 발행합니다.")
