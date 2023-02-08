for x in range(10):
    T=int(input())
    ladder=[list(map(int,input().split()))for _ in range(100)]

    #미로의 입구를 찾을 때 처럼 출구에서부터 위로 올라가며 정답 입구를 탐색
    start=0
    depth=99 #가장 아래에서부터 시작
    ans=0
    for j in range(100):
        if ladder[depth][j]==2: #가장 아래 행을 탐색해서 원소가 2인 위치의 j가 탐색을 시작할 출발지점
            start=j

    while True: #가장 위의 행에 도착할때까지 반복문 실행
        depth-=1 # depth=99의 가장 아래에서 위로 한칸씩 올라감

        #위로 올라가며 왼쪽이나 오른쪽으로 이동 했을때 길(1)이 있다면 길이 끝날때 까지
        #해당 방향으로 이동
        if 0<=start-1 and ladder[depth][start-1]==1:
            while True:
                start-=1
                if ladder[depth][start-1]!=1:
                    break

        elif start+1<100 and ladder[depth][start+1]==1:
            while True:
                start += 1
                if start==99 or ladder[depth][start+1]!=1:
                    break

        if depth==0: #위로 올라가다가 가장 위쪽 행렬에 도착하면 반복을 중지하고 탈출
            ans=start
            break

    print(f'#{T} {ans}')