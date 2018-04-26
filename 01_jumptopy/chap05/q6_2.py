def baesu(i):
    list123 = []
    num_list1 = []
    for num_list1 in range(int(num_list[i]), int(num_list[0]) + int(num_list[i]), int(num_list[i])):
        list123.append(num_list1)
    return list123

while(True):
    sum = 0
    num_list = input("범위, 첫 번째 수, 두 번째 수를 입력하세요.(종료 : 프로그램 종료) : ").split()
    if(num_list[0] == '종료'):
        break
    print("0부터 %d이하의 범위를 선택하셨습니다. 이중에서" % int(num_list[0]))
    print("%d의 배수는 %s입니다." %(int(num_list[1]), baesu(1)))
    print("%d의 배수는 %s입니다." %(int(num_list[2]), baesu(2)))
    a = list(set(baesu(1)+baesu(2)))
    for list0 in a:
        sum += list0
    print("%d와 %d의 배수는 %s입니다." % (int(num_list[1]),int(num_list[2]), a))
    print("따라서 0부터 %d이하의 범위내에서 %d과 %d의 배수의 총합은 %d입니다" %(int(num_list[0]),int(num_list[1]),int(num_list[2]), sum))








