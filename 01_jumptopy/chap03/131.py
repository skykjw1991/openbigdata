# coding: cp949
student_name_lists=[
        ('��','����'),
        ('��','���'),
        ('��','����'),
        ('��','ȿ��'),
        ('��','����')
        ]

#print(student_name_lists)


    
search=input("�˻��ϰ����ϴ� ���� �Է��ϼ��� : ")
is_found_flag=False
for (last_name,first_name) in student_name_lists:
    if search == last_name:
        if is_found_flag==False:
            print("<<�˻����>>")
            is_found_flag=True
        print(last_name+first_name)
    
