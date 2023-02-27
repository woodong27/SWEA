T=int(input())

from pprint import pprint

for tc in range(T):
    N,M=map(int,input().split())
    flag=[list(input())for _ in range(N)]
    pprint(flag)

    ans=0
    for j in range(M):
        if flag[0][j]!='W':
            ans+=1
        if flag[N-1][j]!='R':
            ans+=1

    print(ans)