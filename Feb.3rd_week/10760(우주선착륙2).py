T=int(input())

di=[-1,1,0,0,-1,-1,1,1]
dj=[0,0,-1,1,-1,1,1,-1] #상,하,좌,우,11시,1시,5시,7시

for tc in range(T):
    N,M=map(int,input().split())
    pic=[list(map(int,input().split()))for _ in range(N)]

    ans=0
    for i in range(N):
        for j in range(M):
            stack=[]
            for k in range(8):
                if 0<=i+di[k]<N and 0<=j+dj[k]<M and pic[i+di[k]][j+dj[k]]<pic[i][j]:
                    stack.append(pic[i+di[k]][j+dj[k]])
            print(i,j,stack)
            if len(stack)>=4:
                ans+=1

    print(f'#{tc+1} {ans}')