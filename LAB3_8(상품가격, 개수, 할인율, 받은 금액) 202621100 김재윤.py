product_price=int(input("상품의 가격:"))
product_amount=int(input("상품의 개수:"))
discount=int(input("할인율(%):"))

get_money= int(input("받은 금액:"))
print("거스름돈:", get_money-(product_price*product_amount*(1-discount/100)))