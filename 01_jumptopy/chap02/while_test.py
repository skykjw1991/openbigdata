# coding: cp949
order_list = [
        "¥���2",
        "«��2, ¥���1",
        "¥���1",
        "«¥��2",
        "�Ⱥ�ä1, ������2",
        "������1, ������1"]
print("""���� ������ ���� ���� ȯ���մϴ�.
        ���ݱ��� �ֹ�����Ʈ�Դϴ�.""")
print(order_list)

print("\n���ݺ��� �丮�� �����ϰڽ��ϴ�.")
while order_list:
    print("'"+order_list.pop(0)+"'�丮�� �Ϸ�Ǿ����ϴ�.")

print("��� �ֹ��� ���Ͽ� ó���ϰڽ��ϴ�.")