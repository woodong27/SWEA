T=int(input())

def bf(sentence,word):
    i,j=0,0 #i는 문장의 길이, j는 찾으려는 단어의 길이
    n=len(sentence)
    m=len(word)
    ans=0
    while i<n and j<m:
        if word[j]!=sentence[i]:
            i=i-j
            j=-1
        i+=1
        j+=1

        if j==m:
            j=0
            ans=1
            break

    return ans

for x in range(T):
    str1=input() #word
    str2=input() #sentence

    print(f'#{x+1} {bf(str2,str1)}')

