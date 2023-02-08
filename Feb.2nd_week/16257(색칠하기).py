T=int(input())

for x in range(T):
    lst = [[0 for y in range(10)]for y in range(10)]
    N=int(input())

    for k in range(N):
        ls=list(map(int,input().split()))

        for n in range(ls[0],ls[2]+1):
            for m in range(ls[1],ls[3]+1):
                lst[n][m]+=ls[4]

    count=0
    for i in range(10):
        for j in range(10):
            if lst[i][j]>=3: #빨간색과 파란색이 칠해져서 값이 3이상인 위치의 수를 세어줌
                count+=1

    print(f'#{x+1} {count}')