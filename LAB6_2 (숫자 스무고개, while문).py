print('1부터 10 사이의 숫자를 맞추시오')
import random

c= random.randint(1,10)
count = 0

while True:
    a= int(input("숫자를 입력하시오:"))
    count += 1
    if a < c:
        print("낮음!")
    elif a > c:
        print("높음!")
    elif a == c:
        print("축하합니다.")
        print("시도 횟수:", count)
        break
         
         
            
            
    