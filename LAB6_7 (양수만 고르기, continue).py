price_list = [12000, -5000, 30000, 0, 15000, -200, 5000]

hap = 0

for i in price_list:
    if i <= 0:
        continue
    hap += i

print(hap)
    