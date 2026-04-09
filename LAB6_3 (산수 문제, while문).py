import random

while True:
    n1 = random.randint (1,99)
    n2 = random.randint (1,99)

    a= int(input(f'{n1}+{n2}= '))
    
    if n1+n2 == a:
        print("잘했어요!!")
    else:
        print("틀렸어요. 복습하세요.")
        break
