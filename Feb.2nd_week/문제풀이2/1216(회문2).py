for _ in range(10):
    T=int(input())
    lst=[list(input())for x in range(100)]

    col=[]
    for i in range(100):
        col.append(''.join(lst[i]))

    row=[]
    for i in range(100):
        for j in range(100):
            if i<j:
                lst[i][j],lst[j][i]=lst[j][i],lst[i][j]

    for i in range(100):
        row.append(''.join(lst[i]))

    ans=0
    for i in range(100):
        start=0
        j=0
        while start+j<100:
            j+=1
            if col[i][start:start+j+1]==col[i][start:start+j+1][::-1]:
                if len(col[i][start:start+j+1])>=ans:
                    ans=len(col[i][start:start+j+1])

            if row[i][start:start+j+1]==row[i][start:start+j+1][::-1]:
                if len(row[i][start:start+j+1])>=ans:
                    ans=len(row[i][start:start+j+1])

            if start+j==100:
                start+=1
                j=0

    print(f'#{T} {ans}')