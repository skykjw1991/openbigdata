def read_content():
    f1= open('D:\\bigdata\\python_workspace\\openbigdata\\01_jumptopy\\chap05\\poll.txt', 'r')
    line = f1.read()
    print(line)
    f1.close()

try:
    read_content()
except FileNotFoundError:
    while(True):
        print("기존 poll.txt 파일을 찾을 수 없습니다. 아래중 선택하세요.")
        no = int(input("1. 종료 2. 새로운 파일 생성 3. 변경된 파일 경로 입력 : "))
        if(no == 1):
            break
        elif(no == 2):
            while (True):
                f2 = open('D:\\bigdata\\python_workspace\\openbigdata\\01_jumptopy\\chap05\\poll.txt', 'a')
                why = input("프로그래밍이 왜 좋으세요? (종료 입력시 프로그램 종료) : ")
                if (why == '종료'):
                    break
                else:
                    name = input("이름이 무엇입니까? ")
                    print("설문에 응답해 주셔서 감사합니다")
                    f2.write("[%s] %s \n" % (name, why))
                    f2.close()
                    read_content()
            f2.close()
        elif(no == 3):
            abc = input("변경된 파일 경로를 입력하세요. : ")
            while(True):
                path = abc + '\\poll.txt'
                f3 = open( path , 'a')
                why = input("프로그래밍이 왜 좋으세요? (종료 입력시 프로그램 종료) : ")
                if (why == '종료'):
                    break
                else:
                    name = input("이름이 무엇입니까? ")
                    print("설문에 응답해 주셔서 감사합니다")
                    f3.write("[%s] %s \n" % (name, why))
                    f3.close()
                    f3 = open(path , 'r')
                    line = f3.read()
                    print(line)
                    f3.close()
            f3.close()