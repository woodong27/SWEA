T=int(input())

for tc in range(T):
    N,M=map(int,input().split())
    flag=[list(input())for _ in range(N)]

    minv=N*M
    for i in range(0,N-2):
        for j in range(1,N-1-i):
            cnt=0
            for ii in range(i+1):
                for jj in range(M):
                    if flag[ii][jj]!='W':
                        cnt+=1

            for ii in range(i+1,i+j+1):
                for jj in range(M):
                    if flag[ii][jj]!='B':
                        cnt+=1

            for ii in range(i+j+1,N):
                for jj in range(M):
                    if flag[ii][jj]!='R':
                        cnt+=1

            if cnt<minv:
                minv=cnt

    print(f'#{tc+1} {minv}')