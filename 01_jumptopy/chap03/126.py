# coding: cp949

coffee=10
money=300

while money:
    print("���� �޾����� Ŀ�Ǹ� �ݴϴ�.")
    coffee=coffee-1

    print("���� Ŀ���� ���� %d���Դϴ�." %coffee)

    if not coffee:
        print("Ŀ�ǰ� �� ���������ϴ�. �ǸŸ� �����մϴ�.")
        break
