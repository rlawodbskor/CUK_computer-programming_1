number_list= [2, 5, 4, 4, 8, 3, 16, 2, 32, 1]
i=0
while i < len(number_list): #리스트 길이= 10, 0,2,4,6,8일 때만 반복, len은 데이터 길이를 알려주는 함수
    print(number_list [i], number_list [i+1])
    i += 2