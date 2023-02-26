T=int(input())

for tc in range(T):
    N,M,K=map(int,input().split())

    people=list(map(int,input().split()))

    bread=M*K
    print(len(people),N)
    print(bread)
