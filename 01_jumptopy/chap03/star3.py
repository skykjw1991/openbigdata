# coding: cp949

print("������ ��� ���α׷� ver3.0")

star = int(input("Ȧ���� �Է��ϼ���(0 <- ����): "))
while True:
    if star%2 !=0:
        print(star*"-"+"--")
        for i in range(1, int(star/2)+1):
            print("|" + " "*(int(star/2)-i+1) + "*"*(2*i-1) + " "*(int(star/2)-i+1)+ "|")
        for j in range(int(star/2)+1,0,-1):
            print("|" + " "*(int(star/2)-j+1) + "*"*(2*j-1)+ " "*(int(star/2)-j+1)+ "|")
        print(star*"-"+"--")
        break
    else:
        break
