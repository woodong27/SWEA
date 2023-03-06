from collections import deque

T=int(input())

delta=((-1,0),(1,0),(0,-1),(0,1))

def makingroad(si,sj):
    q=deque([(si,sj,1,0,0)])
    global ans
    while q:
        ci,cj,cnt,cut,flag=q.popleft()
        if cnt>ans:
            ans=cnt
        for di,dj in delta:
            ni,nj=ci+di,cj+dj
            if 0<=ni<N and 0<=nj<N:
                if mountain[ni][nj]>=mountain[ci][cj]-cut:
                    if not flag:
                        k=1
                        while k<=K:
                            if mountain[ni][nj]-k<mountain[ci][cj]-cut:
                                q.append((ni,nj,cnt+1,k,1))
                                break
                            k+=1
                else:
                    q.append((ni,nj,cnt+1,0,flag))

for tc in range(T):
    N,K=map(int,input().split())

    mountain=[list(map(int,input().split()))for _ in range(N)]

    highest=0
    for i in range(N):
        for j in range(N):
            if mountain[i][j]>highest:
                highest=mountain[i][j]

    hpos=[]
    for i in range(N):
        for j in range(N):
            if mountain[i][j]==highest:
                hpos.append((i,j))

    ans=0
    while hpos:
        hi,hj=hpos.pop()
        makingroad(hi,hj)

    print(f'#{tc+1} {ans}')