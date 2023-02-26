T=int(input())

def search(lst):
    global ans
    for i in range(N):
        cnt=0
        for j in range(N):
            if lst[i][j]=='1':
                cnt+=1
            else:
                if cnt==K:
                    ans+=1
                cnt=0

            if j==N-1 and cnt==K:
                ans+=1

for tc in range(T):
    N,K=map(int,input().split())

    puzzle=[list(input().split())for _ in range(N)]
    puzzle_t=list(map(list,zip(*puzzle)))

    ans=0
    search(puzzle)
    search(puzzle_t)

    print(f'#{tc+1} {ans}')