T=int(input())

def bf(p,t):
    i=0 #t의 인덱스
    j=0 #p의 인덱스
    N=len(t) #t의 길이
    M=len(p) #p의 길이
    count=0
    idx=[]
    while i<N and j<M:
        if p[j]!=t[i]:
            i=i-j
            j=-1
        i+=1
        j+=1

        if j==M:
            count+=1
            j=0
            idx.append(i-M)
    return count,idx

for x in range(T):
    t,p=map(str,input().split())
    cnt,index=bf(p,t)
    lst_t=list(t)

    for i in range(len(index)):
        for j in range(len(p)):
            lst_t.pop(index[i]+j)

    print(cnt)
    print(index)
    print(lst_t)