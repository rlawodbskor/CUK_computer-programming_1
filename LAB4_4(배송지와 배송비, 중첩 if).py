place= input("배송지(현재는 Korea와 US만 가능):")
total_price=int(input("상품의 가격:"))

if place=="Korea":
    if total_price<=20000:
        print("배송비는 3000원입니다.")
    else:
        print("배송비는 0원입니다.")
    
if place=="US":
    if total_price<=100000:
        print("배송비는 8000원입니다.")
    else:
        print("배송비는 0원입니다.")