product_price=int(input("상품의 가격:"))
product_quantity=int(input("상품의 개수:"))
sale_ratio=int(input("할인율(%):"))

get_money=int(input("받은 금액:"))
change=int(get_money-(product_price*product_quantity*(1-sale_ratio/100)))
print("거스름돈:",int(change))
print("500원=",int(change//500),", 100원=",int((change%1000)//100),", 10원=", int((change%1000%100)//10),", 1원=",int((change%1000%100%10)//1),sep='')

