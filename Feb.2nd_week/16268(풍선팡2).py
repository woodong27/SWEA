T=int(input())

di = [-1,1,0,0] #방향 배열
dj = [0,0,-1,1]

for x in range(T):
    N,M=map(int,input().split())
    lst=[list(map(int,input().split()))for x in range(N)]

    result=[]

    for i in range(N):
        for j in range(M):
            sum=lst[i][j] #상하좌우 이동을 시작하는 원점의 값을 sum에 할당
            for k in range(4):
                ni,nj=i+di[k],j+dj[k]
                if 0<=ni<N and 0<=nj<M:
                    sum+=lst[ni][nj] #sum에 상하좌우 이동한 위치의 원소들을 더해줌
                result.append(sum) #결과 리스트에 sum을 넣어주고

    print(f'#{x+1} {max(result)}') #result리스트에서 가장 큰 값을 답으로 출력