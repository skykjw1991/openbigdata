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

if 4<=age<=65:
    pay_type=int(input("��� ������ �����ϼ���. (1:���� 2: ���� ���� �ſ� ī��) : "))
    if pay_type==1:
        if 4<=age<=65:
            pay=int(input("����� �Է��ϼ��� : "))
            if money > pay:
                print("%d�� ���ڶ��ϴ�. �Է��Ͻ� %d�� ��ȯ�մϴ�" %(-(pay-money), pay))
            elif money == pay:
                print("�����մϴ�. Ƽ���� �����մϴ�.")
            else :
                print("�����մϴ�. Ƽ���� �����ϰ� �Ž����� %d�� ��ȯ�մϴ�" %(-(money-pay)))
        else :
            print("�����մϴ�. Ƽ���� �����մϴ�.")

    elif pay_type==2:
        print("�����ݾ��� 10% ����, 60~65�� ����� �߰� 5% ����")
        if 60<=age<=65:
            print("%d�� ���� �Ǿ����ϴ�. Ƽ���� �����մϴ�." %(money*0.90*0.95))
        else:
            print("%d�� ���� �Ǿ����ϴ�. Ƽ���� �����մϴ�." %(money*0.90))

    else:
        print("�ٽ� �����ϼ���")
else:
    print("�����մϴ�. Ƽ���� �����մϴ�.")
