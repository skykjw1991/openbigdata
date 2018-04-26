import csv
import math

def get_cvs_colInstance(col_name):
    col_instance=[]
    col_index = data[0].index(col_name)
    for row in data[1:]:
        col_instance.append(row[col_index])
    return col_instance

def print_row(col_instance, type="int"):
    if type=="int":
        list(map(int,col_instance))
    elif type == "float":
        list(map(float,col_instance))
    elif type == "str":
        list(map(int,col_instance))

    for row_element in col_instance:
        print(row_element)

def print_clo(row_instance):
   for row_element in row_instance:
        print(row_element, end="")


while True:
    with open('Demographic_Statistics_By_Zip_Code.csv', newline="") as infile:
        data = list(csv.reader(infile))
    num=int(input("\n\n0.종료 1.행 2.열 3.총합 4.평균 5.최대값 6.최소값 7.편차 8.표준편차 9.분산 10.오름차순 정렬 11.내림차순 정렬 \n 메뉴를 선택하세요 : "))
    if num==0:
        break
    elif num==1:
        row = int(input("Access Key를 입력하세요 : "))
        #print_clo(data[row])

        for row in "JURISDICTION NAME":
            print_clo(data[row])

    elif num==2:
        col = input("Access Key를 입력하세요 : ")
        print_row(get_cvs_colInstance(col))

    elif num==3:
        sum1 = input("Access Key를 입력하세요 : ")
        print_row(get_cvs_colInstance(sum1))
        col_instance = []
        col_index = data[0].index(sum1)
        # for row in data[1:]:
        #     col_instance.append(int(row[col_index]))
        # print(sum(row))
        if type == "str":
            list(map(int, col_instance))
        elif type == "int":
            list(map(int, col_instance))
        elif type == "float":
            list(map(float, col_instance))
        for row in data[1:]:
            #print(sum(row))
            col_instance.append(row[col_index])
        print(sum(col_instance))