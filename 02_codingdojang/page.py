# coding: cp949

m=int(input("�ѰǼ�(m)�� �Է��Ͻÿ�: "))
n=int(input("���������� ������ �Խù���(n)�� �Է��Ͻÿ�(n>=1): "))


while True:
    if m>n:
        if m%n==0:
            print("���: ",int(m/n))
        else:
            print("���: ", int(m/n)+1)
    elif m==0:
        print("���: ", m)
    else:
        print("���: ", int(1))
    break    
    
