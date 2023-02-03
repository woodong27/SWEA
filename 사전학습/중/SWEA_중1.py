# for i in range(len(l1)):
#     l1[i] = sorted(l1[i])
num=int(input()) #테스트케이스의 수
l1=[0 for x in range(num)]
for i in range(num): #2중 배열 리스트 생성
    a=int(input()) #테스트케이스의 번호
    l1[a-1]=list(map(int,input().split()))

mode=[0 for x in range(10)] #최빈수 저장 리스트(0으로 초기화)
max_count=[0 for x in range(10)] #최빈수를 판단하기 위해 count하는 리스트(0으로 초기화)

for i in range(num):
    for j in range(101): #0~100까지 수를 비교하며 최빈수를 찾음
        count=0
        for k in l1[i]:
            if j==k:
                count=count+1

        if max_count[i]<=count:
            max_count[i]=count
            mode[i]=j

for x in range(10):
    print(f'#{x+1} {mode[x]}')
