# coding: cp949

name = "������,���翵,����ǥ,���翵,�ڹ�ȣ,������,���翵,������,�ֽ���,�̼���,�ڿ���,�ڹ�ȣ,������,����ȯ,���缺,������,������"

print("1. �� : ",name.count('��'), "�� : ", name.count('��'))
print('2. "���翵"�̶� �̸��� �� �� �ݺ��ǳ���? : ', name.count('���翵'))
result =name.split(',')
aSet=set(result)
remove=list(aSet)
print("3. �ߺ��� ������ �̸��� ����ϼ��� : ", remove)
remove.sort()
print("4. ������������ �����Ͽ� ����ϼ��� : ", remove)
