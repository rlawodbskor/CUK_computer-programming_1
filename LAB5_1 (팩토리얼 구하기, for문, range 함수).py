x= int(input("정수를 입력하시오:"))
result=x
for i in range(x-1,0,-1):
    result*=i
print(x,"!은",result,"이다.")