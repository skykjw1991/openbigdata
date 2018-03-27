class Restaurant:

    def __init__(self,name,type):
        self.restaurant_name = name
        self.cuisine_type = type

    def describe_restaurant(self,restaurant_name, cuisine_type):
        print("저희 레스토랑 명칭은 '%s'이고 %s 전문점입니다. " %(self.restaurant_name, cuisine_type))

    def open_restaurant(self,restaurant_name):
        print("저희 %s 레스토랑이 오픈했습니다."%(self.restaurant_name))

    def __del__(self,name1):
        self.restaurant_name = name1
        print("%s 레스토랑 문닫습니다."%(self.restaurant_name))
i=0
list_a=['0','0','0']
while(i<4):


    print("레스토랑 이름과 요리 종류를 선택하세요.(공백으로 구분): ")
    name,type=input().split()
    list_a[i] = name
    one = Restaurant(name,type)
    one.describe_restaurant(name,type)
    one.open_restaurant(name)
    i=i+1

    if(i == 3):
        print("저녁 10시가 되었습니다.")
        one.__del__(list_a[0])
        one.__del__(list_a[1])
        one.__del__(list_a[2])
        break
    else:
        continue



