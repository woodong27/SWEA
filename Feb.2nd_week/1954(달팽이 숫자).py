T=int(input())

for t in range(T):
    N=int(input())
    snail=[[0 for _ in range(N)]for _ in range(N)]

    step=1
    size=N
    count=0
    x=-1
    y=0

    while size>0:
        for i in range(size):
            x+=step
            count+=1
            snail[y][x]=count

        size-=1

        for i in range(size):
            y+=step
            count+=1
            snail[y][x]=count

        step*=-1

    print(f'#{t+1}')
    for j in range(N):
        print(*snail[j])