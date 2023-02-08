for x in range(10):
    T=int(input())
    l=[[0 for x in range(100)]for x in range(100)]
    for k in range(100):
        l[k]=list(map(int,input().split()))

    col=[0 for x in range(100)] #각 행의 합을 받아줄 리스트
    for i in range(100):
        for j in range(100):
            row[i]=row[i]+l[i][j]

    row=[0 for x in range(100)] #열의 합을 받아줄 리스트
    for i in range(100):
        for j in range(100):
            col[i]=col[i]+l[j][i]

    diag=[0 for x in range(2)] #대각선의 합을 받을 리스트
    for i in range(2):
        for j in range(100):
            diag[i]=diag[i]+l[j][j]

    ans=[max(row),max(col),max(diag)] #각 리스트의 가장 큰 값을 ans배열에 넣어주고

    print(f'#{x+1} {max(ans)}') #ans배열에서 가장 큰 값을 정답으로 출력
