from collections import deque

T=int(input())

di=[-1,1,0,0]
dj=[0,0,-1,1]

def bfs():
    visited=[[0 for _ in range(N)]for _ in range(N)]
    que=deque([])
    que.append((si,sj,-1))
    while que:
        ci,cj,cnt=que.popleft()
        if ci==gi and cj==gj:
            return cnt
        visited[ci][cj]=1
        for k in range(4):
            if 0<=ci+di[k]<N and 0<=cj+dj[k]<N:
                ni=ci+di[k]
                nj=cj+dj[k]
                if maze[ni][nj]!='1' and not visited[ni][nj]:
                    que.append((ni,nj,cnt+1))

    return 0

for tc in range(T):
    N=int(input())
    maze=[list(input())for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if maze[i][j]=='2':
                si,sj=i,j
            if maze[i][j]=='3':
                gi,gj=i,j

    result=bfs()
    print(f'#{tc+1} {result}')