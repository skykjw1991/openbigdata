# coding: cp949

print("������ ��� ���α׷� ver1.0")

star = int(input("Ȧ���� �Է��ϼ���(0 <- ����): "))
while True:
    if star%2 !=0:
        for i in range(1, star+1):
            print(" "*(star-i) + "*"*(2*i-1))
        break
    else:
        break

