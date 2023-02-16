T=int(input())

def divide(lst):
    if len(lst)==1:
        return lst

def winner(lst):
    if abs(lst[0]-lst[1])==2:
        return min(lst)

    elif abs(lst[0]-lst[1])==1:
        return max(lst)




for x in range(T):
    N=int(input())
    cards=list(map(int,input().split()))


