def GuGu(num):
    i =1
    while i<10:
        print("%d * %d = %d" %(int(num) , i, int(num)*i))
        i=i+1

while True:
    num = input("\n숫자를 입력하세요. (-1:종료, all: 구구단 전체 출력) : ")
    if num == 'all':
        j=2
        while j<10:
            GuGu(j)
            j=j+1
            print("\n")
    elif int(num)<=-2:
        raise ValueError("양수를 입력하세요")
    elif int(num) == -1:
        break
    else:
        GuGu(num)