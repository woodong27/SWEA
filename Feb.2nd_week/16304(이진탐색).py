T=int(input())

for x in range(T):
    P,A,B=map(int,input().split())
    ca,cb=0,0

    l,r=1,P
    while l<=r:
        c=(l+r)//2
        if c==A:
            ca+=1
            break
        elif c>A:
            r=c
            ca+=1
        else:
            l=c
            ca+=1

    l,r=1,P
    while l<=r:
        c=(l+r)//2
        if c==B:
            cb+=1
            break
        elif c>B:
            r=c
            cb+=1
        else:
            l=c
            cb+=1

    if ca<cb:
        ans='A'
    elif ca>cb:
        ans='B'
    else:
        ans=0

    print(f'#{x+1} {ans}')