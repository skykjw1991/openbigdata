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
    pay=int(input("요금을 입력하세요 : "))
    if money > pay:
        print("%d가 모자랍니다. 입력하신 %d를 반환합니다" %(-(pay-money), pay))
    elif money == pay:
        print("감사합니다. 티켓을 발행합니다.")
    else :
        print("감사합니다. 티켓을 발행하고 거스름돈 %d를 반환합니다" %(-(money-pay)))
else :
    print("감사합니다. 티켓을 발행합니다.")

