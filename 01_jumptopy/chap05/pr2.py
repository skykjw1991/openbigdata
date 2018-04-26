
count = 0

while(True):
    count = count + 1
    hi = int(input("안녕하세요. 이름을 입력하세요 : "))
    if(count == 1):
        print("Hi [%s]!! You are %dst person come here!"%(hi, count))
    elif(count ==2 ):
        print("Hi [%s]!! You are %dnd person come here!"%(hi, count))
    elif(count ==3):
        print("Hi [%s]!! You are %drd person come here!"%(hi, count))
    elif(4<= count <=10):
        print("Hi [%s]!! You are %d th person come here!"%(hi, count))
    elif(count>10):
        print("Sorry [%s]. The event is closed because You are %dth person come here."%(hi, count))
