nums = [1, 2, 4, 7]

find = False

for i in nums:
    if i == 4:
        find = True
        break

if find:
    print('찾았다!')
else:
    print('없다!')