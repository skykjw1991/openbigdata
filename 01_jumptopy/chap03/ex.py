#coding: cp949

money=int(input("������ ��� �ݾ��� �Է��ϼ���: "))
card=int(input("�ſ�ī�带 �����ϰ� ��ʴϱ�? (1:��, 2:�ƴϿ�): "))

print("�Է� ���� �м�")
print("\n���� ������ ��� �ݾ��� "+str(money)+"�� �Դϴ�.")

if card==1:
	print("�ſ�ī�带 �����ϰ� ��ʴϴ�.")
else:
	print("���� �ſ�ī�尡 �����ϴ�.")

print("\n�м� ���")
if money >=3000 or card==1:
	print("�ýø� Ÿ�� ���� �� �ֽ��ϴ�.")
else:
	print("�ɾ� ���ô°� ���ڳ׿�.")

