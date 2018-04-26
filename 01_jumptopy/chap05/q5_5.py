while(True):
    is_error = False
    num_list = input("\n안녕하세요 두수를 입력하세요(종료:프로그램 종료): ").split()
    if (num_list[0] == '종료'):
        break

    try:
        num_list[0]=int(num_list[0])
    except ValueError:
        is_error = True
        print("죄송합니다. 첫번째 입력이 '[%s]' 입니다. 숫자를 입력하세요. "%num_list[0])

    try:
        num_list[1]=int(num_list[1])
    except ValueError:
        is_error = True
        print("죄송합니다. 두번째 입력이 '[%s]' 입니다. 숫자를 입력하세요. "%num_list[1])

    if(num_list[1] == 0):
        try:
            num_list[0] / num_list[1]
        except ZeroDivisionError:
            is_error = True
            print("죄송합니다. 두번째 입력에서 0을 입력하셨습니다. 분모는 0이 되어서는 안됩니다.")


    if is_error == False:
        print(int(num_list[0]) + int(num_list[1]))
        print(int(num_list[0]) - int(num_list[1]))
        print(int(num_list[0]) * int(num_list[1]))
        print(int(num_list[0]) / int(num_list[1]))

