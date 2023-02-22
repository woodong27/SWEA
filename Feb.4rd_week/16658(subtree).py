T=int(input())

def counting(start):
    global cnt
    if start==0:
        return
    else:
        cnt+=1
        counting(c1[start])
        counting(c2[start])

for tc in range(T):
    E,N=map(int,input().split())
    lst=list(map(int,input().split()))

    c1=[0]*(E+2)
    c2=[0]*(E+2)
    for i in range(0,E*2,2):
        if c1[lst[i]]:
            c2[lst[i]]=lst[i+1]
        else:
            c1[lst[i]]=lst[i+1]

    cnt=0
    counting(N)
    print(f'#{tc+1} {cnt}')