T=int(input()) #테스트 케이스의 갯수
for x in range(T): #T번 반복
    N,M=map(int,input().split())
    l1=list(map(int,input().split())) #첫번째 리스트
    l2=list(map(int,input().split())) #두번째 리스트

    max=0 #최대값을 반환할 변수

    if len(l1)==len(l2): #두 리스트의 길이가 동일할 때
        for i in range(len(l1)):
            max=max+l1[i]*l2[i]

    elif len(l1)>len(l2): #l1이 l2보다 길때
        for i in range(len(l1)-len(l2)+1):
            temp=0 #계산값을 임시로 저장할 변수(반복문이 시작될 때마다 0으로 초기화 됨)
            if i==0: #처음에는 인덱스별로 곱해서 더해주면 됨
                for j in range(len(l2)):
                    temp=temp+l1[j]*l2[j]
            elif i>=1: #두번째 반복부터는 l2를 뒤로 한칸씩 밀어줌
                l2.insert(i-1,0)
                for j in range(len(l2)):
                    temp=temp+l1[j]*l2[j]

            if temp>=max: #현재 max보다 temp가 더 크면 max값을 변경해줌
                max=temp

    elif len(l1)<len(l2): #l2가 l1보다 길때
        for i in range(len(l2) - len(l1) + 1):
            temp = 0
            if i == 0:
                for j in range(len(l1)):
                    temp = temp + l1[j] * l2[j]
            elif i >= 1:
                l1.insert(i-1,0)
                for j in range(len(l1)):
                    temp = temp + l1[j] * l2[j]

            if temp >= max:
                max = temp

    print(f'#{x+1} {max}')