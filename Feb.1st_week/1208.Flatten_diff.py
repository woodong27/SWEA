for x in range(10):
    dump=int(input())
    lst=list(map(int,input().split()))

    for i in range(dump):
        maxv = lst.pop(lst.index(max(lst))) #현재 리스트의 최대값을 pop
        minv = lst.pop(lst.index(min(lst))) #현재 리스트의 최소값을 pop
        maxv-=1
        minv+=1
        lst.append(maxv)
        lst.append(minv)

    print(f'#{x + 1} {max(lst)-min(lst)}')

    '''
    #pop(인덱스번호)
    #list.index(리스트의 원소) -> 해당 원소의 인덱스를 찾아 줌
    
    또다른 방법
    for i in range(dump):
        lst[lst.index(max(lst))]-=1
        lst[lst.index(min(lst))]+=1
        
    '''

