class Restaurant:

    def __init__(self,name,type):
        self.restaurant_name = name
        self.cuisine_type = type

    def describe_restaurant(self,restaurant_name, cuisine_type):
        print("저희 레스토랑 명칭은 '%s'이고 %s 전문점입니다. " %(self.restaurant_name, cuisine_type))

    def open_restaurant(self,restaurat_name):
        print("저희 %s 레스토랑이 오픈했습니다."%(self.restaurant_name))

print("레스토랑 이름과 요리 종류를 선택하세요.(공백으로 구분): ")
name,type=input().split()

one = Restaurant(name,type)
one.describe_restaurant(name,type)
one.open_restaurant(name)
