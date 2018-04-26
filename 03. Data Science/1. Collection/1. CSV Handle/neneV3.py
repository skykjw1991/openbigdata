import urllib.request
import os
from pandas import DataFrame
import xml.etree.ElementTree as ET
import datetime

now = datetime.datetime.now()                   #현재시간
nowDatetime = now.strftime('%Y-%m-%d_%H%M%S')   #년월일 시분초

dir_name = "V3_BigData"     #디렉토리 이름
dir_delimiter = "\\"        #구분자
nene_dir = "Nene_Data"      #디렉토리 이름(하위)
nene_file = nowDatetime     #csv이름(시분초)
csv = ".csv"                #csv파일확장자
record_limit = 3            #디렉토리 하위 저장파일 갯수
result = []                 #리스트 생성

def make_dir(index) :                           #디렉토리 생성 규칙
    os.mkdir(dir_name + dir_delimiter + nene_dir+str(index))
    return None

def make_nene(dir_index, file_index) :          #파일 생성 규칙
    destination_csv = dir_name + dir_delimiter + nene_dir + str(dir_index) + dir_delimiter + nene_file + csv;
    nene_table.to_csv(destination_csv,encoding="cp949", mode='w', index=True)
    return None

response = urllib.request.urlopen('http://nenechicken.com/subpage/where_list.asp?target_step2=%s&proc_type=step1&target_step1=%s'%(urllib.parse.quote('전체'),urllib.parse.quote('전체')))
xml = response.read().decode('UTF-8')
root = ET.fromstring(xml)

for element in root.findall('item'):
    store_name = element.findtext('aname1')         #매장 이름
    store_sido = element.findtext('aname2')         #시, 도
    store_gungu = element.findtext('aname3')        #군, 구
    store_address = element.findtext('aname5')      #매장 주소
    result.append([store_name]+[store_sido]+[store_gungu]+[store_address])

nene_table = DataFrame(result,columns=('sotre','sido','gungu','store_address'))

try : os.mkdir(dir_name)
except : pass
try :
    with open(dir_name + dir_delimiter + "nene_index.txt", 'r') as file :       #nene_index 읽어서 디렉토리 생성 및 구분
        file_index = file.readline()
        file_index = int(file_index)
        dir_index = int(file_index / record_limit)
        if file_index % record_limit != 0 :
            dir_index = dir_index+1
        if file_index % record_limit == 1 :
            make_dir(dir_index)

        make_nene(dir_index, file_index)
        file_index += 1
    with open(dir_name + dir_delimiter + "nene_index.txt", 'w') as file :       #file_index 증가 값 쓰기
        file.write(str(file_index))
except FileNotFoundError :          #파일이 없을경우 새로 생성
    with open(dir_name + dir_delimiter + "nene_index.txt", 'w') as file :
        file.write('2')
    make_dir(1)
    make_nene(1, 1)
print("End")