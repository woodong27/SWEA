T=int(input())

for tc in range(T):
    strings=list(input())

    stack=[]
    for string in strings:
        if string=='{' or string=='(':
            stack.append(string)

        elif string==')':
            if stack and stack[-1]=='(':
                stack.pop()
            else:
                stack.append(string)

        elif string=='}':
            if stack and stack[-1]=='{':
                stack.pop()
            else:
                stack.append(string)

    print(f'#{tc+1} {0 if len(stack)>0 else 1}')