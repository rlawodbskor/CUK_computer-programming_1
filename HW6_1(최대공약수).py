n1 = int(input("정수 1 입력: "))
n2 = int(input("정수 2 입력: "))

if n1 < n2: #n1이 n2보다 작으면 둘이 위치를 바꿔라
    n1, n2 = n2, n1

while n2 != 0:
    n1, n2 = n2, n1 % n2 #n1&n2를 다시 n2와 n1을 n2로 나눈 나머지로 설

if n1 == 1:
    print("두 수는 서로소이다")
else:
    print("두 수의 최대공약수:", n1)