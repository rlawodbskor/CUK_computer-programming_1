x_input=int(input("첫번째 정수를 입력하시오.:"))
y_input=int(input("두번째 정수를 입력하시오.:"))

if x_input % y_input == 0:
    print(y_input,"는",x_input, "의 약수입니다.")
else:
    print(y_input,"는",x_input, "의 약수가 아닙니다.")