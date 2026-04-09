n = int(input("몇 번째 항까지 구할까요? "))
a = 1
b = 1

for i in range(n):
    if i == n - 1: #0부터 시작하니까 n-1이 마지막 항이 된다.
        print(a)
    else:
        print(a, end=', ')
    a, b = b, a + b