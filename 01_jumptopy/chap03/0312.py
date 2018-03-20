# coding: cp949

money = 0
age=int(input("나이를 입력하세요 : "))
while True:
    if 0 <= age <= 3:
        money += 0
    elif 4 <= age <= 13:
        money += 2000
    elif 14<= age <= 18:
        money += 3000
    elif 19<=age<=65:
        money += 5000
    else:
        money += 0
    
    print("요금은"+money+ "입니다")
