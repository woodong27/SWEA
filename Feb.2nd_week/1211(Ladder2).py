for x in range(10):
    t=int(input())
    ladder=[list(map(int,input().split()))for _ in range(100)]

    ans=0
    cnt=100**2 #정답을 받기위한 변수(작은 값과 비교해야 하기 때문에 처음에 큰 값을 할당해줌

    #ladder1과는 달리 위에서부터 아래로 내려가며 최단거리를 찾아야함
    for i in range(100):
        depth = 0 #깊이가 0으로 가장 위쪽 행에서부터 시작
        start = i
        if ladder[depth][i]==1: #가장 첫 행에서 원소가 1인 열이 출발지점
            count=0 #출구까지 가는동안 몇번 이동했는지 세어주기 위한 변수

            while depth!=99: #마지막 행에 도착할때까지 반복
                count+=1
                depth+=1

                #Ladder1과 마찬가지로 이동하면서 왼쪽/오른쪽에 1(길)이 있다면
                #길이 끝날때 까지 계속해서 해당 방향으로 이동
                if 0<start-1 and ladder[depth][start-1]==1:
                    while True:
                        start-=1
                        count+=1
                        if 0>start-1 or ladder[depth][start-1]!=1:
                            break

                elif start+1<100 and ladder[depth][start+1]==1:
                    while True:
                        start+=1
                        count+=1
                        if start==99 or ladder[depth][start+1]!=1:
                            break

        if cnt>count: #만약 총 이동한 거리인 count가 cnt보다 작으면 cnt를 재할당 해주고
            cnt=count
            ans=i     #가장 짧은 구간의 시작점이었던 i를 정답으로 출력

    print(f'#{t} {ans}')