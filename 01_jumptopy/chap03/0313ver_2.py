# coding: cp949

money =0
grade =0
age=int(input("���̸� �Է��ϼ��� : "))

if 0 <= age <= 3:
    money=0
    grade="����"
elif 4 <= age <= 13:
    money=2000
    grade="���"
elif 14<= age <= 18:
    money=3000
    grade="û�ҳ�"
elif 19<=age<=65:
    money=5000
    grade="����"
elif 66 <= age:
    money=0
    grade="����"
else:
    print("�ٽ��Է��ϼ���")

print("���ϴ� %s ����̸�, ����� %d �� �Դϴ�" %(grade, money))




