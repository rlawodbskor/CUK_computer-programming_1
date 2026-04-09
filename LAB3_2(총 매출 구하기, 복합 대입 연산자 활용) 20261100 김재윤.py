total_price = 0

milk_total = int(input("판매된 우유의 개수=")) * 2000
coke_total = int(input("판매된 콜라의 개수=")) * 3000
kimbap_total = int(input("판매된 김밥의 개수=")) * 3500

total_price += milk_total
total_price += coke_total
total_price += kimbap_total

print("오늘 총 매출은", total_price, "원입니다.")