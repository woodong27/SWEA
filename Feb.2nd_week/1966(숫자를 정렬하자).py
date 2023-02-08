T=int(input())
for x in range(T):
    N=int(input())
    lst=list(map(int,input().split()))

    #lst.sort()

    #sort직접 구현하기
    for i in range(len(lst)):
        for j in range(i+1,len(lst)):
            if lst[i]>=lst[j]:
                lst[i],lst[j]=lst[j],lst[i]

    print(f'#{x+1}',*lst)