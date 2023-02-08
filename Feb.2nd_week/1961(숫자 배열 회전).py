T=int(input())

def rotate_90_degree(list,n): #리스트를 90도 회전시켜주는 함수
    rotated_l=[[0 for x in range(n)]for x in range(n)]
    for a in range(n):
        for b in range(n):
            rotated_l[b][n-1-a]=list[a][b] #90도 회전하면 index가 이렇게 바귐

    return rotated_l

for x in range(T):
    N=int(input())
    l=[list(map(int,input().split()))for _ in range(N)]
    ans=[[]for _ in range(N)] #답으로 출력하기 위한 리스트

    l_90=rotate_90_degree(l,N) #90도 돌린 리스트
    l_180=rotate_90_degree(l_90,N) #180도 돌린 리스트
    l_270=rotate_90_degree(l_180,N) #270도 돌린 리스트

    for i in range(N):
        for j in range(N):
            ans[i].append(str(l_90[i][j])) #ans리스트의 i행에 90도 회전시킨 리스트의 i행을 순서대로 넣어줌
        ans[i].append(' ')

        for j in range(N):
            ans[i].append(str(l_180[i][j])) #ans리스트의 i행에 180도 회전시킨 리스트의 i행을 순서대로 넣어줌
        ans[i].append(' ')

        for j in range(N):
            ans[i].append(str(l_270[i][j])) ##ans리스트의 i행에 270도 회전시킨 리스트의 i행을 순서대로 넣어줌

        #모든 리스트의 마지막 행까지 ans에 넣어준 후 순서대로 출력하면 완료
    for i in range(N):
        ans[i]=''.join(ans[i]) #출력을 편하게 하기 위해 ans리스트의 i행의 리스트를 하나의 문자열로 묶어줌

    print(f'#{x+1}')
    for i in range(N):
        print(ans[i])