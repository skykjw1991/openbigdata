# coding: cp949

money =0
grade =0
count =0
init_ticket=3
init_dc=5

while True:
    age=int(input("���̸� �Է��ϼ��� : "))
    if 0 <= age <= 3:
        money=0
        grade="����"
    elif 4 <= age <= 13:
        money=2000
        grade="���"
        count += 1
    elif 14<= age <= 18:
        money=3000
        grade="û�ҳ�"
        count += 1
    elif 19<=age<=65:
        money=5000
        grade="����"
        count += 1
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
            count -= 1
    else:
        print("�����մϴ�. Ƽ���� �����մϴ�.")
        continue

    if count ==7 or count==14 or count==21:
        print("�����մϴ�. 1�ֳ� �̺�Ʈ�� ��÷�Ǿ����ϴ�. ���� ����Ƽ���� �����մϴ�. �ܿ� ����Ƽ�� %d��" %(init_ticket -1))
        init_ticket -=1
    elif count ==4 or count==8 or count==12 or count==16 or count ==20:
        print("�����մϴ�. ����ȸ���� ���� �̺�Ʈ�� ��÷�Ǽ̽��ϴ�. ���� ȸ�� ���� Ƽ���� �����մϴ�. �ܿ� ����Ƽ�� %d��" %(init_dc -1))
        init_dc -=1

