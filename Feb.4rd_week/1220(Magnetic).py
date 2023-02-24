from pprint import pprint

for tc in range(1,11):
    N=int(input())
    table=[list(map(int,input().split()))for _ in range(N)]

    # pprint(table,indent=1,width=1000)
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
            k=1
            if table[i][j]==1:
                table[i][j]=0
                while i+k<N:
                    if table[i+k][j]==1:
                        table[i+k][j]=0
                    elif table[i+k][j]==2:
                        result+=1
                        break
                    k+=1

            elif table[i][j]==2:
                table[i][j]=0
                while 0<=i-k:
                    if table[i-k][j]==2:
                        table[i-k][j]=0
                    if table[i-k][j]==1:
                        result+=1
                        break
                    k+=1

    print(f'#{tc} {result}')