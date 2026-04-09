number_1= int(input("수1 입력:"))
number_2= int(input("수2 입력:"))
number_3= int(input("수3 입력:"))

if number_1 > number_2 > number_3:
    print(number_1, ",", number_2, ",", number_3, "중 최대값은", number_1, "이다.")
elif number_1> number_3> number_2:
    print(number_1, ",", number_2, ",", number_3, "중 최대값은", number_1, "이다.")
elif number_2 > number_3 > number_1:
    print(number_1, ",", number_2, ",", number_3, "중 최대값은", number_2, "이다.")
elif number_2 > number_1 > number_3:
    print(number_1, ",", number_2, ",", number_3, "중 최대값은", number_2, "이다.")
elif number_3 > number_2 > number_1:
    print(number_1, ",", number_2, ",", number_3, "중 최대값은", number_3, "이다.")
elif number_3 > number_1 > number_2:
    print(number_1, ",", number_2, ",", number_3, "중 최대값은", number_3, "이다.")
    
#확률과 통계에서 배웠던 내용을 바탕으로 3개의 수를 모두 나열하는 경우의 수인 3!을 사용했는데 이렇게 하는게 맞나요?
#아니면 다른 계산식으로 더 짧은 코드를 쓸 수 있나요?
#max_value= a if (a >= b and a >= c) else (b if b >= c else c)
#print(max_value)