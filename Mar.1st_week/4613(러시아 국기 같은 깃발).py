T=int(input())

for tc in range(T):
    N,M=map(int,input().split())
    flag=[list(input())for _ in range(N)]

    '''
    w:흰색을 칠할 범위
    b:파란색을 칠할 범위
    w+b이후부터 N까지 나머지 범위에 빨간색을 칠해줌
    '''
    minv=N*M
    for w in range(0,N-2):
        for b in range(1,N-1-w):
            cnt=0
            for i in range(w+1):
                for j in range(M):
                    if flag[i][j]!='W':
                        cnt+=1

            for i in range(w+1,w+b+1):
                for j in range(M):
                    if flag[i][j]!='B':
                        cnt+=1

            for i in range(w+b+1,N):
                for j in range(M):
                    if flag[i][j]!='R':
                        cnt+=1

            if cnt<minv:
                minv=cnt

    print(f'#{tc+1} {minv}')