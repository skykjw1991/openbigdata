# coding: cp949

age=int(input("���̸� �Է��ϼ��� : "))
while True:
    if 0 <= age <= 3:
        print("����� �����Դϴ�")
        break
    elif 4 <= age <= 13:
        print("����� 2000���Դϴ�")
        break
    elif 14<= age <= 18:
        print("����� 3000���Դϴ�")
        break
    elif 19<=age<=65:
        print("�����5000���Դϴ�")
        break
    else:
        print("����� �����Դϴ�")
        break
