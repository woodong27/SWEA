from collections import deque

T=int(input())

di=[-1,1,0,0]
dj=[0,0,-1,1]

def bfs(si,sj):
    visited=[[0 for _ in range(N)]for _ in range(N)]
    q=deque()
    q.append((si,sj,1))
    distances=[]
    while q:
        ci,cj,cnt=q.popleft()
        visited[ci][cj]=1
        distances.append((rooms[si][sj],cnt))
        for k in range(4):
            ni,nj=ci+di[k],cj+dj[k]
            if 0<=ni<N and 0<=nj<N:
                if not visited[ni][nj] and rooms[ni][nj]-rooms[ci][cj]==1:
                    q.append((ni,nj,cnt+1))

    return distances

for tc in range(T):
    N=int(input())
    rooms=[list(map(int,input().split()))for _ in range(N)]

    resultd,resultv=0,N**2
    for i in range(N):
        for j in range(N):
            print(bfs(i,j))

    print(f'#{tc+1}',resultv,resultd)