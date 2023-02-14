T=int(input())

def DFS(graph,start_node,end_node,cnt):
    global result
    visited[start_node]=True
    if start_node==end_node:
        result=cnt

    for i in range(1,V+1):
        if i in graph[start_node] and not visited[i]:
            DFS(graph,i,end_node,cnt+1)

for x in range(T):
    V,E=map(int,input().split())
    graph=[[]for _ in range(V+1)]
    for i in range(E):
        v1,v2=map(int,input().split())
        graph[v1].append(v2)
    S,G=map(int,input().split())

    visited=[False]*(V+1)
    result,cnt=0,0
    DFS(graph,S,G,cnt)

    print(f'#{x+1} {1 if result>0 else 0}')