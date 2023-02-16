T=int(input())
from pprint import pprint

di=[-1,1,0,0,-1,-1,1,1]
dj=[0,0,-1,1,-1,1,1,-1] #상,하,좌,우,11시,1시,5시,7시

for tc in range(T):
    N,M=map(int,input().split())

    board=[[0 for _ in range(N)]for _ in range(N)]
    board[N//2-1][N//2-1]=2
    board[N//2-1][N//2]=1
    board[N//2][N//2-1]=1
    board[N//2][N//2]=2

    pprint(board,indent=1,width=15)


    for x in range(M):
        temp_i,temp_j,color=map(int,input().split())
        i,j=temp_i-1,temp_j-1
        board[i][j]=color
        for k in range(8):
            if 0<=i+di[k]<N and 0<=j+dj[k]<N:
                ni,nj=i+di[k],j+dj[k]


    pprint(board, indent=1, width=15)

    print(f'#{tc+1}')