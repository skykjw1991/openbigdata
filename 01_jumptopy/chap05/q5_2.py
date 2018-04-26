f = open('D:\\bigdata\\python_workspace\\openbigdata\\01_jumptopy\\chap05\\poll.txt', 'w')

while(True):
    why = input("프로그래밍이 왜 좋으세요? (종료 입력시 프로그램 종료) : ")
    if(why=='종료'):
        break

    else:
        name = input("이름이 무엇입니까? ")
        print("설문에 응답해 주셔서 감사합니다")
        f.write("[%s] %s \n" % (name, why))
f.close()