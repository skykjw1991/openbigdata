# coding: cp949


student_marks=[]
number=1
while number<=5:
    student_mark=input(str(number)+"�� �л����� �Է��ϼ��� : ")
    student_marks.append(int(student_mark))
    number = number+1

  
number=1
for student_mark in student_marks:
    if student_mark >=60:
        print("%d�� �л� %d��, �հ��Դϴ�." %(number,student_mark))
    else:
        print("%d�� �л� %d��, ���հ��Դϴ�." %(number,student_mark))

    number=number+1
