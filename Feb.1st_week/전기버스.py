T=int(input())

for x in range(T):
    K,N,M=map(int,input().split())
    charger=list(map(int,input().split()))
    station=[]
    for i in range(N+1):
        if i in charger:
            station.append(str(i))
        else:
            station.append(i)
    print(station)
    count=0
    K_copy=K
    i=0
    while i<=N:
        # if K<charger[0] or charger[-1]+K<N:
        #     break
        # else:
        #     for j in range(len(charger)-1):
        #         if charger[j]+K<charger[j+1]:
        #             break
        K-=1
        i+=1
        if K==0:
            if station[i]==str(station[i]):
                K=K_copy
                count+=1
            else:
                for j in range(1,K+1):
                    if station[i-j]==str(station[i-j]):
                        K=K_copy
                        i=i-j
                        count+=1

    print(f'#{x+1} {count}')
