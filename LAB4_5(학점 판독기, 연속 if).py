score= int(input("점수를 입력하시오:"))

if score >= 70:
    if score >= 90:
        print("A학점 입니다.")
    if score >= 80:
        print("B학점 입니다.")
    else:
        print ("C학점 입니다.")
else:
    print("F학점 입니다.")