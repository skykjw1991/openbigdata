# coding: cp949
my_str="파이썬"
#my_str=" "
my_list=[1,2,3]
#my_list=[]
my_tuple=(1,2,3)
#my_tuple=()
my_dic={"추미애":"더불어 민주당","안철수":"바른미래당"}
my_num=100
#my_num=0
my_num=None

print("예제1] 문자열(String) 파일의 True/False")
print("my_str: "+my_str)
if my_str:
    print("True")
else:
    print("False")

print("\n예제2] 리스트(List) 파일의 True/False")
print("my_list: ",end='')
print(my_list)
if my_list:
    print("True")
else:
    print("False")

print("\n예제3] 튜플(Tuple) 파일의 True/False")
print("my_Tuple: ",end='')
print(my_tuple)
if my_tuple:
    print("True")
else:
    print("False")

print("\n예제4] 덕셔너리(Dictionary) 파일의 True/False")
print("my_dic: ",end='')
print(my_dic)
if my_dic:
    print("True")
else:
    print("False")

print("\n예제5] 숫자형(Integer) 파일의 True/False")
print("my_num: ",end='')
print(my_num)
if my_num:
    print("True")
else:
    print("False")
print("\n프로그램 종료")
