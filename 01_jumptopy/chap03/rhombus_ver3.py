# coding: cp949

output_msg="Ȧ���� �Է��ϼ���(0 <- ����): "
blank=" "
star="*"
horizontal_line="-"
vertical_line="|"
print("������ ��� ���α׷� ver3.0")
print("")

while True:
  print(output_msg,end='')
  customer_input = int (input())
  if customer_input == 0:
       print("")
       print("������ ���α׷� ����� �̿��� �ּż� �����մϴ�.")
       break
  elif customer_input % 2 == 0:
      print("¦���� �Է��ϼ̽��ϴ�. ���Է� ��Ź�帳�ϴ�.")
      continue
  else:
      star_count = 1
      blank_count = int((customer_input - star_count)/2)
      print(blank,end='')
      print(horizontal_line*customer_input,end='')
      print(blank)
      while True:
            print(vertical_line,end='')
            print(blank*blank_count,end='')
            print(star*star_count,end='')
            print(blank*blank_count,end='')
            print(vertical_line)
            if star_count == customer_input:
                break
            star_count += 2
            blank_count -= 1
      while True:
          if star_count == 1:
              break
          star_count -= 2
          blank_count += 1
          print(vertical_line,end='')
          print(blank*blank_count,end='')
          print(star*star_count,end='')
          print(blank*blank_count,end='')
          print(vertical_line)

      print(blank,end='')
      print(horizontal_line*customer_input,end='')
      print(blank)