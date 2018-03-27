class Restaurant:

    def __init__(self,name,type):
        self.restaurant_name = name
        self.cuisine_type = type

    def describe_restaurant(self,restaurant_name, cuisine_type):
        print("저희 레스토랑 명칭은 '%s'이고 %s 전문점입니다. " %(self.restaurant_name, cuisine_type))

    def open_restaurant(self,restaurat_name):
        print("저희 %s 레스토랑이 오픈했습니다."%(self.restaurant_name))

    def reset_number_served(self):
        self.number_served = 0

    def increment_number_served(self,people):
        self.number_served=+people

    def check_customer_number(self,check):
        self.check_customer_number=check

print("레스토랑 이름과 요리 종류를 선택하세요.(공백으로 구분): ")
name,type=input().split()
one = Restaurant(name,type)
one.describe_restaurant(name,type)


number_served=0

openres=input("레스토랑을 오픈하시겠습니까? (y/n) : ")
if (openres == 'y'):
    one.open_restaurant(name)

    while(True):
        people=input("어서오세요. 몇명이십니까?(초기화:0입력, 종료:-1, 누적고객 확인:p) : ")
        if (people == "0"):
            print("손님 카운팅을 0으로 초기화 하였습니다.")
            number_served=0
            continue
        elif (people == "-1"):
            print("%s 레스토랑 문닫습니다."%name)
            break
        elif (people == "p"):
#            number_served =+ number_served
            print("지금까지 총 %d명 손님께서 오셨습니다."%number_served)
        else:
            print("손님 %d명 들어오셨습니다. 자리를 안내해 드리겠습니다."%int(people))
            number_served=+ int(people)

