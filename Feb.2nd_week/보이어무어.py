tc=int(input())
target=input()
sentence=input()

skip=list(target)[::-1]
print(skip)

t=len(target) #t=3
s=len(sentence)

start=0
count=0
i=0
while start<=s:
    jump=0
    start+=t-1
    if sentence[start-i]!=skip[i]:
        while i<t-1:
            i+=1
            if sentence[start-i]==skip[i]:
                break
        start+=i
    else:
        i=0
        while i<t-1:


