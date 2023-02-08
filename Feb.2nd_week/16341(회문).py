T=int(input())

for x in range(T):
    ans=0
    N,M=map(int,input().split())
    lst=[0 for _ in range(N)]
    for i in range(N):
        lst[i]=list(input())

    #1979번과 마찬가지로 행과 열 리스트를 따로 만들어서 각 리스트에서 비교해줌
    row=[]
    col=[]
    for i in range(N):
        row_w=[]
        col_w=[]
        for j in range(N):
            col_w.append(lst[i][j])
            row_w.append(lst[j][i])
        row.append(row_w)
        col.append(col_w)

    for i in range(N): #행과 열 리스트에서 M개씩 쪼개서 반대로 읽었을때와 바로 읽었을때 값이 같다면 ans에 해당 문자열을 저장
        for j in range(N-M+1):
            if row[i][j:j+M]==row[i][j:j+M][::-1]:
                ans=''.join(row[i][j:j+M])
            elif col[i][j:j+M]==col[i][j:j+M][::-1]:
                ans=''.join(col[i][j:j+M])

    print(f'#{x+1} {ans}')
