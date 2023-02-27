T=int(input())

hexa_to_bi={'0':'0000','1':'0001','2':'0010','3':'0011',
            '4':'0100','5':'0101','6':'0110','7':'0111',
            '8':'1000','9':'1001','A':'1010','B':'1011',
            'C':'1100','D':'1101','E':'1110','F':'1111'}

codes={'0001101':0,'0011001':1,'0010011':2,'0111101':3,'0100011':4,
       '0110001':5,'0101111':6,'0111011':7,'0110111':8,'0001011':9}

for tc in range(T):
    N,M=map(int,input().split())

    password=[list(input())for _ in range(N)]

    code=[]
    for i in range(N):
        for j in range(M):
            if password[i][j]!='0':
                temp=[]
                a=0
                while j+a<M and password[i][j+a]!='0':
                    temp.append(password[i][j+a])
                    a+=1

                trans=''.join(temp)
                if trans not in code and not len(trans)%7:
                    code.append(trans)

    print(code)