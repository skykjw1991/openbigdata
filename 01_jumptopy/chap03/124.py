# coding: cp949

prompt="""
1. �߰�
2. ����
3. ����Ʈ
4. ����

���ڸ� �Է��ϼ���: """

number=0

while number !=4:
    number=int(input(prompt))
    
    if number==1:
        print("'1. �߰�' �޴��� �����ϼ̽��ϴ�")
    elif number==2:
        print("'2. ����' �޴��� �����ϼ̽��ϴ�")
    elif number==3:
        print("'3. ����Ʈ' �޴��� �����ϼ̽��ϴ�")
    elif number==4:
        print("'4. ����' �޴��� �����ϼ̽��ϴ�")
    else:
        print("1~4 �޴��� �����մϴ�")
