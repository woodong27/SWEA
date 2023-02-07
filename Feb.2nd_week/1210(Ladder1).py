for x in range(10):
    T=int(input())
    ladder=[list(map(int,input().split()))for _ in range(100)]

    start=0
    depth=99
    ans=0
    for j in range(100):
        if ladder[depth][j]==2:
            start=j

    while True:
        if ladder[depth-1][start]==1:
            depth-=1

            if 0<=start-1 and ladder[depth][start-1]==1:
                while True:
                    start-=1
                    if ladder[depth][start-1]!=1:
                        break

            elif start+1<100 and ladder[depth][start+1]==1:
                while True:
                    start += 1
                    if start==99 or ladder[depth][start+1]!=1:
                        break

            if depth == 0:
                ans = start
                break

    print(f'#{T} {ans}')