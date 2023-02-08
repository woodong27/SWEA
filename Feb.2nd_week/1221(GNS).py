T=int(input())

words_lst=['ZRO','ONE','TWO','THR','FOR','FIV','SIX','SVN','EGT','NIN']

for x in range(T):
    tc,N=map(str,input().split())
    words=list(map(str,input().split())) #단어들을 입력받은 리스트
    print(f'{tc}')

    for i in words_lst: #word_lst의 원소들을 처음부터 끝까지 순서대로 탐색
        count=0
        for j in words:
            if i==j: #words리스트 안에 i가 있으면 카운트를 증가시키고
                count+=1
        print((i+' ')*count) #증가한 count횟수만큼 i를 출력