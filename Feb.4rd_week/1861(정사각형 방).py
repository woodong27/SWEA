from collections import deque

T=int(input())

di=[-1,1,0,0]
dj=[0,0,-1,1]

def bfs(si,sj):
    visited=[[0 for _ in range(N)]for _ in range(N)]
    q=deque()
    q.append((si,sj,1))
    visited[si][sj]=1
    distances=[]
    while q:
        ci,cj,cnt=q.popleft()
        distances.append((rooms[si][sj],cnt))
        for k in range(4):
            ni,nj=ci+di[k],cj+dj[k]
            if 0<=ni<N and 0<=nj<N and rooms[ni][nj]-rooms[ci][cj]==1:
                if not visited[ni][nj]:
                    q.append((ni,nj,cnt+1))
                    visited[ni][nj]=1

    return distances

import time

for tc in range(T):
    start=time.time()
    N=int(input())
    rooms=[list(map(int,input().split()))for _ in range(N)]

    resultd,resultv=0,N**2
    result=0
    for i in range(N):
        for j in range(N):
            if not result:
                result=bfs(i,j)
            elif len(bfs(i,j))>len(result):
                result=bfs(i,j)
            elif len(bfs(i,j))==len(result):
                if result[0][0]>bfs(i,j)[0][0]:
                    result=bfs(i,j)

    end=time.time()
    print(f'#{tc+1} {result[-1][0]} {result[-1][1]} // 실행시간 : {end-start}초')