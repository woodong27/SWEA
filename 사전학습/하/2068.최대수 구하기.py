n=int(input()) #테스트 케이스의 갯수
list=[[int(x) for x in input().split()] for row in range(n)] #2중 배열 입력받음
for i in range(len(list)):
    list[i]=sorted(list[i]) #2중 배열 정렬

for i in range(n):
    print(f'#{i+1}',list[i][-1]) #정렬된 리스트에서 각 index의 가장 마지막 숫자 출력