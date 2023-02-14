T = int(input())

for x in range(T):
    N = int(input())

    lst = []
    for i in range(N):
        c, g = map(int, input().split())
        lst.append(c)
        lst.append(g)

    stack = []
    stack.append(lst[0])
    for i in range(1, N * 2):

        if stack[-1] <= lst[i]:
            stack.pop()
            stack.append(lst[i])
        else:
            stack.append(lst[i])

    print(f'#{x + 1} {len(stack)}')