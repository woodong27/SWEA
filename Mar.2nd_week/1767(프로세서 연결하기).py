T=int(input())

from collections import deque

delta=((0,-1),(0,1),(1,0),(-1,0))

def connect(point):
    global ans
    while point:
        ci,cj=point.pop()
        temp=N
        for di,dj in delta:
            cnt=0
            for m in range(1,N):
                ni,nj=ci+di*m,cj+dj*m
                if 0<=ni<N and 0<=nj<N and cells[ni][nj] not in ['x','s']:
                    if cells[ni][nj]==0:
                        cnt+=1
                    elif not 0<=ni+di<N or not 0<=nj+dj<N:
                        if temp>cnt:
                            temp=cnt

        ans+=temp

def counting(si,sj):
    temp=N
    for di,dj in delta:
        for m in range(1,N):
            ni,nj=si+di*m,sj+dj*m
            if 0<=ni<N and 0<=nj<N:
                if cells[ni][nj] in ['x','s',0]:
                    break

                elif not 0<=ni+di<N or not 0<=nj+dj<N:
                    if cells[ni][nj]<temp:
                        temp=cells[ni][nj]

    return temp


for tc in range(T):
    N=int(input())
    cells=[list(map(int,input().split()))for _ in range(N)]

    start=[]
    for i in range(0,N):
        for j in range(0,N):
            if (i==0 or i==N-1) or (j==0 or j==N-1):
                if cells[i][j]==1:
                    cells[i][j]='x'
            elif cells[i][j]==1:
                start.append((i,j,0))
                cells[i][j]='s'

    ans=0
    connect(start)
    print(ans)
