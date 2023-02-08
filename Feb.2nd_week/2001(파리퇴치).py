T=int(input())
for x in range(T):
    N,M=map(int,input().split())
    lst=[list(map(int,input().split()))for _ in range(N)]

    #탐색하는 원점을 기준으로 M*M크기의 행렬을 탐색하기 위한 방향배열
    di=[x for x in range(M)]*M
    di.sort()
    dj=[x for x in range(M)]*M

    result=[]

    for i in range(N-M+1):
        for j in range(N-M+1):
            killed=0
            for k in range(len(di)):
                ni,nj=i+di[k],j+dj[k]
                killed+=lst[ni][nj]
            result.append(killed)

    print(f'#{x+1} {max(result)}')