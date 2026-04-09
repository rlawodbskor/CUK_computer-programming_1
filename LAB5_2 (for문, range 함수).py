i = 0

while True:
    n = int(input('숫자를 입력하시오: '))
    i += n
    
    a = input('계속?(yes/no): ')
    if a != 'yes':
        break

print("합계는", i, "입니다.")

# n = int(input('숫자를 입력하시오:'))
# 
# i = n
# a = 'yes'
# 
# while a == 'yes':
#     i += n
#     a = input('계속?(yes/no): ')
# 
# print("합계는", i, "입니다.")
