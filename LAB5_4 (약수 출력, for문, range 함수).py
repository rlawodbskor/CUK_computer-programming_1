x = int(input("자연수 입력: "))

for i in range(1, x+1):
    if x % i == 0:
        print(i, end=' ')