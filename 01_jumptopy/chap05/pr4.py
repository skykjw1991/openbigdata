
while(True):
    num_list = input("세 개의 양수를 입력하세요(종료 -1) : ").split()

    if(num_list[0] == '-1'):
        break

    elif(int(num_list[2])%int(num_list[0])== 0 and int(num_list[2])%int(num_list[1])==0):
        print("%s는 %s와 %s의 공배수 입니다."%(num_list[2], num_list[0], num_list[1]))

    else:
        print("%s는 %s와 %s의 공배수가 아닙니다." % (num_list[2], num_list[0], num_list[1]))



