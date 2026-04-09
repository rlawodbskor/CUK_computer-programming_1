text = input("문자열 입력:")

count=0
for ch in text:
    if ch == 'a' or ch == 'e' or ch =='i' or ch == 'o' or ch =='u':
        count += 1
print("모음 개수:", count)

#for ch in text:
#      if ch in 'aeiou':
#            count+=1
#print("모음 개수:", count)