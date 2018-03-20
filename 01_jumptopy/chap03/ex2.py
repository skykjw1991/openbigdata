# coding: cp949


student_marks=[]
number=1
while number<=5:
    student_mark=input(str(number)+"번 학생점수 입력하세요 : ")
    student_marks.append(int(student_mark))
    number = number+1

  
number=1
for student_mark in student_marks:
    if student_mark >=60:
        print("%d번 학생 %d점, 합격입니다." %(number,student_mark))
    else:
        print("%d번 학생 %d점, 불합격입니다." %(number,student_mark))

    number=number+1
