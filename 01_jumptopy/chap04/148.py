def sum_mul(choice,*args):
    if choice == "sum":
        result = 0
        for i in args:
            result = result+i
    elif choice=="mul":
        result=1
        for i in args:
            result =result*i
    elif choice=="sub":
        result=18
        for i in args:
            result=result-i
    elif choice =="div":
        result=100
        for i in args:
            result=result/i

    return result


result = sum_mul("sum",1,2,3,4,5)
print(result)

result=sum_mul("mul",1,2,3,4,5)
print(result)

result=sum_mul("sub",10,5,2)
print(result)

result=sum_mul("div",10,5,2)
print(result)