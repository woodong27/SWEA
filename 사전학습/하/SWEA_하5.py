n=int(input()) #테스트 케이스의 갯수
list=[[int(x) for x in input().split()] for row in range(n)] #2중 배열 리스트 생성

for i in range(n): #각 행의 원소를 모두 더하고 10으로 나눠서 평균값 출력
    print(f'#{i+1}',round(sum(list[i])/10))