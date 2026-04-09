print('369 게임 시작!')
print("규칙: 숫자를 입력하거나 '짝'을 입력하세요.")

i = 1 #i는 1부터 시작

while True: #틀릴 때까지 계속
    # 사용자 차례 정답
    if '3' in str(i) or '6' in str(i) or '9' in str(i):
        answer = "짝"
    else:
        answer = str(i)

    user = input(f"{i} -> 사용자 차례: ")

    if user != answer:
        print(f"틀렸습니다! 정답은 '{answer}' 입니다.")
        break

    i += 1

    # 컴퓨터 차례
    if '3' in str(i) or '6' in str(i) or '9' in str(i):
        print("컴퓨터: 짝")
    else:
        print("컴퓨터:", i)

    i += 1