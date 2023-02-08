T=int(input())

for x in range(T):
    N,K=map(int,input().split())
    puzzle=[list(map(int,input().split()))for _ in range(N)]

    col=[] # 각 행(가로)을 저장할 리스트
    row=[] # 각 열(세로)을 저장할 리스트
    for i in range(N):
        col_w=[]
        row_w=[]
        for j in range(N):
            col_w.append(str(puzzle[i][j]))
            row_w.append(str(puzzle[j][i]))
        col.append(''.join(row_w))
        row.append(''.join(col_w))

    for i in range(N):
        row[i]=row[i].split('0') #0을 기준으로 문자열을 쪼개서 연속된 1만 남게 됨
        col[i]=col[i].split('0')

    count=0
    for i in range(N):
        for j in row[i]: #각 리스트의 원소중에서 문자열의 길이가 K와 같은 문자열이 있으면 count를 증가시켜줌
            if len(j)==K:
                count+=1

        for j in col[i]:
            if len(j)==K:
                count+=1

    print(f'#{x+1} {count}')