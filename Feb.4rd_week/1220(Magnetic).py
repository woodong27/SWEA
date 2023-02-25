for tc in range(1,11):
    N=int(input())
    table=[list(map(int,input().split()))for _ in range(N)]

    #1:N극 자성체->아래로
    #2:S극 자성체->위로
    '''
    자성체를 만나면 극성에 따라서 위와 아래로 이동
    이동하며 같은 극성의 자성체를 만나면 지워주고
    다른 자성체를 만나면 더이상 이동할 수 없기 때문에
    result를 1 늘려주고 이동을 멈춤
    '''

    result=0
    for i in range(N):
        for j in range(N):
            if table[i][j]==1:
                table[i][j]=0
                for ii in range(i+1,N):
                    if table[ii][j]==1:
                        table[ii][j]=0
                    elif table[ii][j]==2:
                        result+=1
                        break

            elif table[i][j]==2:
                table[i][j]=0
                for ii in range(i-1,-1,-1):
                    if table[ii][j]==2:
                        table[ii][j]=0
                    elif table[ii][j]==1:
                        result+=1
                        break

    print(f'#{tc} {result}')