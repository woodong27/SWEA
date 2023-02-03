T=int(input()) #테스트 케이스 갯수

for x in range(T):
    N,M=map(int,input().split())
    lst=list(map(int,input().split()))
    min,max=sum(lst),0
    for i in range(N-M+1):
        temp=0
        for j in range(i,i+M):
            temp=temp+lst[j]

        if temp>=max:
            max=temp
        if temp<=min:
            min=temp

    print(f'#{x+1} {max-min}')