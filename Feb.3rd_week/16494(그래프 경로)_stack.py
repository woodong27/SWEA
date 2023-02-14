def dfs_stack(graph,start,end):
    visited=[False]*(V+1)
    stack=[]
    stack.append(start)

    while stack:
        now=stack.pop()
        if visited[now]==False:
            visited[now]=True
            stack.extend(graph[now])

    return visited[end]

T=int(input())

for x in range(T):
    V,E=map(int,input().split())
    graph=[[]for _ in range(V+1)]
    for i in range(E):
        v1,v2=map(int,input().split())
        graph[v1].append(v2)
    S,G=map(int,input().split())

    print(f'#{x+1} {int(dfs_stack(graph,S,G))}')