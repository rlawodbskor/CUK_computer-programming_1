i = 1

while True:
    user = input(f"{i} → 당신의 입력: ") #당신의 입력이 참일 때

    # 숫자에 3,6,9가 포함되는지 확인
    if '3' in str(i) or '6' in str(i) or '9' in str(i):
        answer = "짝"
    else:
        answer = str(i)

    # 정답 비교
    if user == answer: 
        print("정답!")
        i += 1 #1에서 2로, 2에서 3으로
    else:
        print("틀렸습니다!")
        break #틀리면 멈추기