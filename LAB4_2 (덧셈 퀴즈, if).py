#임의의 어떤 수를 생성하기

import random
n = random.randint(1,100)
m = random.randint(1,100)

print(n, "+", m, "=", end='')
answer = int(input())

if answer == n+m:
    print("맞았습니다.")
else:
    print("틀렸습니다.")

#exp=str(n) + " + " + str(m) + " = "
#answer = int(input(exp))