T=int(input())

for tc in range(T):
    sentence=list(input())

    stack=[]
    for word in sentence:
        if word=='{' or word=='(':
            stack.append(word)

        elif word==')':
            if stack and stack[-1]=='(':
                stack.pop()
            else:
                stack.append(word)

        elif word=='}':
            if stack and stack[-1]=='{':
                stack.pop()
            else:
                stack.append(word)

    print(f'#{tc+1} {0 if len(stack)>0 else 1}')