T=int(input())

for tc in range(T):
    N,K=map(int,input().split())

    signal=list(map(int,input().split()))
    password=list(map(int,input().split()))

    result=[]
    i=0
    for num in password:
        while i<N:
            if num==signal[i]:
                result.append(num)
                break
            i+=1

    ans=0
    if result==password:
        ans=1
    print(f'#{tc+1} {ans}')