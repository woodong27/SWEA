for x in range(10):
    N=int(input())
    eq=list(input())

    print(eq)
    stack=[]
    sym=[]
    for i in eq:
        if i.isdigit():
            stack.append(int(i))

        else:
            if not sym:
                sym.append(i)
            else:
                if i=='+' and sym[-1]!='*':
                    sym.append(i)
                elif i=='+' and sym[-1]=='*':
                    stack.append(stack.pop()*stack.pop())

    print(stack)
    # print(f'#{x+1} {}')