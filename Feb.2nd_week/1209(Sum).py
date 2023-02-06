for x in range(10):
    T=int(input())
    l=[[0 for x in range(100)]for x in range(100)]
    for k in range(100):
        l[k]=list(map(int,input().split()))

    row=[0 for x in range(100)]
    for i in range(100):
        for j in range(100):
            row[i]=row[i]+l[i][j]

    col=[0 for x in range(100)]
    for i in range(100):
        for j in range(100):
            col[i]=col[i]+l[j][i]

    diag=[0 for x in range(2)]
    for i in range(2):
        for j in range(100):
            diag[i]=diag[i]+l[j][j]

    ans=[max(row),max(col),max(diag)]

    print(f'#{x+1} {max(ans)}')
