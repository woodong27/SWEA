T=int(input())
#내장함수 사용 금지(sort, min, max...etc)
for x in range(T):
    N=int(input())
    lst=list(map(int,input().split()))
    for i in range(N):
        if i%2: #인덱스 번호가 홀수일때
            for j in range(i+1,N):
                if lst[i]>lst[j]: #가장 작은 값이 앞쪽으로 오도록 위치를 변경시켜줌
                    lst[i],lst[j]=lst[j],lst[i]

        else: #인덱스 번호가 짝수 일때
            for j in range(i+1,N):
                if lst[i]<lst[j]: #가장 큰 값이 앞쪽으로 오도록 위치를 변경시켜줌
                    lst[i],lst[j]=lst[j],lst[i]

    if len(lst)>10:
        lst=lst[:10] #리스트의 길이가 10 이상이면 10번째 원소까지만 남겨줌

    print(f'#{x+1}',*lst)
