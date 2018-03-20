# coding: cp949

age=int(input("나이를 입력하세요 : "))
while True:
    if 0 <= age <= 3:
        print("요금은 무료입니다")
        break
    elif 4 <= age <= 13:
        print("요금은 2000원입니다")
        break
    elif 14<= age <= 18:
        print("요금은 3000원입니다")
        break
    elif 19<=age<=65:
        print("요금은5000원입니다")
        break
    else:
        print("요금은 무료입니다")
        break
