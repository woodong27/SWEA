for x in range(10):
    dump=int(input())
    lst=list(map(int,input().split()))
    for i in range(dump):
        lst=sorted(lst)
        if lst[-1]-lst[0]<=1:
            break
        else:
            lst[-1]-=1
            lst[0]+=1

    print(f'#{x+1} {max(lst)-min(lst)}')