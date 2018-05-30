import urllib.request
import datetime
import json

access_key="MQhRVKiNnNgD%2BhgXVPQdKyfQp1vx4ikVDRFzI3rfH20lf5hpUOi2br%2F6%2FppqOgzjtU%2FIPzf2W%2FvMVcOB3rE4sA%3D%3D"

g_Radiator = False
g_Gas_Valve = False
g_Balcony_Windows = False
g_Door = False
g_AI_Mode = False
g_Window = False

def get_request_url(url):
    req = urllib.request.Request(url)
    
    url='http://newsky2.kma.go.kr/service/SecndSrtpdFrcstInfoService2/ForecastTimeData?base_date=20180503&base_time=0951&nx=89&ny=91&_type=json&ServiceKey=MQhRVKiNnNgD%2BhgXVPQdKyfQp1vx4ikVDRFzI3rfH20lf5hpUOi2br%2F6%2FppqOgzjtU%2FIPzf2W%2FvMVcOB3rE4sA%3D%3D&pageNo=1&numOfRows=30'
    #for i in url:
    while True:
        line = url.readline()
        if not line: break
        print(line)



def print_main_menu():
    print("\n1. 장비상태 확인")
    print("2. 장비제어")
    print("3. 스마트모드")
    print("4. 프로그램 종료")
    print("5. 기상정보 출력")

def print_device_status(device_name,devcie_status):
    print("%s 상태: "%device_name, end="")
    if devcie_status == True : print("작동")
    else: print("정지")

def check_device_status():
    print_device_status('난방기',g_Radiator)
    print_device_status('가스밸브', g_Gas_Valve)
    print_device_status('발코니(베란다) 창문', g_Balcony_Windows)
    print_device_status('출입문 상태', g_Door)
    print_device_status('창문 상태', g_Window)

def print_device_menu():
    print("\n상태 변경할 기기를 선택하세요.")
    print("1. 난방기")
    print("2. 가스밸브")
    print("3. 발코니(베란다)창")
    print("4. 출입문")
    print("5. 창문")

def control_device():
    global g_Radiator, g_Gas_Valve, g_Balcony_Windows, g_Door, g_Window

    check_device_status()
    print_device_menu()
    menu_num = int(input("번호를 입력하세요: "))

    if menu_num == 1: g_Radiator = not g_Radiator
    if menu_num == 2: g_Gas_Valve = not g_Gas_Valve
    if menu_num == 3: g_Balcony_Windows = not g_Balcony_Windows
    if menu_num == 4: g_Door = not g_Door
    if menu_num == 5: g_Window = not g_Window

    check_device_status()
#def get_realtime_weather_info():
    #print("자! 메뉴얼 보고 작성해 보세요!")




def smart_mode():
    global g_AI_Mode
    print("1. 인공지능 모드 조회")
    print("2. 인공지능 모드 상태 변경")
    print("3. 실시간 기상정보 Update")
    menu_num = int(input("메뉴를 선택하세요: "))

    if menu_num == 1:
        print("현재 인공지능 모드: ", end='')
        if g_AI_Mode == True: print("작동")
        else:print("중지")
    if menu_num == 2:
        g_AI_Mode = not g_AI_Mode
        print("현재 인공지능 모드: ", end='')
        if g_AI_Mode == True: print("작동")
        else: print("중지")
    #elif menu_num == 3:
        #get_realtime_weather_info()



while True:
    print_main_menu()
    menu_num = int(input("메뉴를 선택하세요: "))

    if(menu_num == 1):
        check_device_status()
    elif(menu_num ==2):
        control_device()
    elif(menu_num == 3):
        smart_mode()
    elif(menu_num == 4):
        break
    # elif(menu_num ==5):
    #     gisang()