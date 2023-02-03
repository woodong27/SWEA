T=int(input())

for x in range(T):
    N=int(input()) # 5<=N<=100
    lst=list(input())

    max, max_num = 0, 0
    for i in range(10):
        count=0
        for j in lst:
            if i==int(j):
                count+=1

            if count>=max:
                max=count
                max_num=i

    print(f'#{x+1} {max_num} {max}')