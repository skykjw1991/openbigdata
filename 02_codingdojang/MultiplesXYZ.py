# coding: cp949

while True:
    sum=0
    num= int(input("�����Ϸ��� 1, �������� 0 : "))
    if num ==1:
        x = int(input("X���� �Է��Ͻÿ� : "))
        y = int(input("Y���� �Է��Ͻÿ� : "))
        z = int(input("���� Z�� �Է��Ͻÿ�: "))
        for three in range(0,z,x):
            sum += three
        for five in range(0,z,y):
            sum += five

        print(sum)
    
    elif num==0:
        break

    else:
        continue

