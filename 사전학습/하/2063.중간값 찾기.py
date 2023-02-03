n=int(input()) #N 입력
score=[int(x) for x in input().split()] #정수를 입력받는 리스트 선언
score.sort() #리스트 정렬
print(score[n//2]) #가운데 숫자 출력