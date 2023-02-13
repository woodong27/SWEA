T=int(input())

for x in range(T):
    line=input()
    line=list(line.replace('()','L'))

    stack=[]
    cnt=0

    for i in line:
        if stack and i=='L':
            cnt+=len(stack)
        elif i=='(':
            stack.append(i)
        elif i==')':
            stack.pop()
            cnt+=1

    print(f'#{x+1} {cnt}')