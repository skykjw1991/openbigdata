# coding: cp949

m=int(input("총건수(m)를 입력하시오: "))
n=int(input("한페이지에 보여줄 게시물수(n)를 입력하시오(n>=1): "))


while True:
    if m>n:
        if m%n==0:
            print("출력: ",int(m/n))
        else:
            print("출력: ", int(m/n)+1)
    elif m==0:
        print("출력: ", m)
    else:
        print("출력: ", int(1))
    break    
    
