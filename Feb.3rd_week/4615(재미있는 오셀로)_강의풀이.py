T=int(input())

di=[-1,1,0,0,-1,-1,1,1]
dj=[0,0,-1,1,-1,1,1,-1] #상,하,좌,우,11시,1시,5시,7시

for tc in range(T):
    N,M=map(int,input().split())

    board=[[0 for _ in range(N+2)]for _ in range(N+2)] #padding 추가
    board[N//2][N//2]=board[N//2+1][N//2+1]=2
    board[N//2][N//2+1]=board[N//2+1][N//2]=1

    for x in range(M):
        i,j,color=map(int,input().split())
        board[i][j]=color
        for k in range(8):
            stack=[] #오셀로를 뒤집어주기 위한 좌표를 저장할 스택
            for m in range(1,N):
                ni,nj=i+di[k]*m,j+dj[k]*m
                if board[ni][nj]==0:
                    break
                elif board[ni][nj]!=color:
                    stack.append((ni,nj))
                else: #뻗어나가다 같은 색깔을 만났을 때 오셀로를 뒤집어 줌
                    while stack:
                        changed=stack.pop()
                        board[changed[0]][changed[1]]=color
                    break

    cntb,cntw=0,0
    for col in board:
        for num in col:
            if num==2:
                cntw+=1
            elif num==1:
                cntb+=1

    print(f'#{tc+1} {cntb} {cntw}')