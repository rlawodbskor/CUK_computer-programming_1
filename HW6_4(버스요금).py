charged_cash= int(input("충전할 금액 입력: "))

while charged_cash >= 1350:
    charged_cash -= 1350
    print ("잔액:", charged_cash)
    if charged_cash < 1350:
        break