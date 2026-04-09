i = 0

while True:
    n = int(input('숫자를 입력하시오: '))
    i += n
    
    a = input('계속?(yes/no): ')
    if a != 'yes':
        break

print("합계는", i, "입니다.")

total = 0
answer = 'yes'
while answer == 'yes':
    number = int(input('숫자를 입력하시오:'))
    total += total+number
    answer = input("계속?")
    if answer == 'no':
        break
print ("합계는", i, "입니다.")
