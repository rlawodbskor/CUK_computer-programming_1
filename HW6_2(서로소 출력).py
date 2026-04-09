for i in range(2, 21):
    count = 0 #약수의 개수 카운팅

    for j in range(1, i + 1): #1부터 i까지 하나씩 꺼내서 나눠보기
        if i % j == 0: #i를 j로 나눈 나머지가 0이라면
            count += 1 #카운트(약수) 하나 추가

    if count == 2: #카운트(약수)가 2개라면 
        print(i, end=' ') #i를 출력