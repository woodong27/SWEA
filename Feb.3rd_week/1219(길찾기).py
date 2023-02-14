def dfs_stack(graph,start,end):
    visited=[0]*(100)
    stack=[]
    stack.append(start)

    while stack:
        now=stack.pop()
        if now==end:
            visited[now]=1
            return visited[now]

        elif visited[now]==0:
            visited[now]=1
            stack.extend(graph[now])

    return visited[end]

for x in range(10):
    S,G=0,99
    tc,N=map(int,input().split())
    lst=list(map(int,input().split()))
    v1=[]
    v2=[]
    for i in range(N*2):
        if i%2:
            v2.append(lst[i])
        else:
            v1.append(lst[i])

    graph=[[]for _ in range(100)]
    for i in range(N):
        graph[v1[i]].append(v2[i])

    print(f'#{tc} {dfs_stack(graph,S,G)}')