for i in range(10):
    tc=int(input())
    lst=[[0]+list(map(int,input().split()))+[0]for _ in range(100)]
    minv=100**2
    '''
    100x100리스트 좌 우에 0으로 된 패딩을 추가해줘서
    좌 우 이동시 인덱스 범위를 벗어나더라도 인덱스 에러가 발생하지 않음
    '''

    for sj in range(1,101):
        si=0
        if lst[si][sj]!=1:
            continue
        cnt,dj=0,0
        ci,cj=si,sj
        while ci<99:
            cnt+=1
            if dj==0:
                if lst[ci][cj-1]==1:
                    dj-=1
                    cj-=1
                elif lst[ci][cj+1]==1:
                    dj=1
                    cj+=1
                else:
                    ci+=1
            else:
                if lst[ci][cj+dj]==1:
                    cj+=1+dj
                else:
                    dj=0
                    ci+=1

        if minv>=cnt:
            minv,ans=cnt,sj-1

    print(f'#{tc} {ans}')