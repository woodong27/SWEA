a=input() #문자열 변수 입력
num=list(a) #입력받은 변수를 리스트로 변환
sum=0

for i in num:
    sum=sum+int(i)
print(sum)