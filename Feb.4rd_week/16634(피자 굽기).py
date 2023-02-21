from collections import deque

T=int(input())

for tc in range(T):
    N,M=map(int,input().split())
    lst=list(map(int,input().split()))

    pizzas=deque([])
    for idx,cheese in enumerate(lst):
        pizzas.append((idx+1,cheese))

    oven=deque([])
    for i in range(N):
        oven.append(pizzas.popleft())

    while oven:
        idx,cheese=oven.popleft()
        cheese//=2
        if cheese!=0:
            oven.append((idx,cheese))
        elif pizzas:
            oven.append(pizzas.popleft())
        elif not oven:
            ans=idx

    print(f'#{tc+1} {ans}')