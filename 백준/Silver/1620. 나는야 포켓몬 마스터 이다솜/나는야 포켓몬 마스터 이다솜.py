N,M = map(int, input().split())

Q = {}
revQ = {}
for i in range(N):
    a = input()
    Q[a]=i+1
    revQ[i+1]=a
    
result=[]
for _ in range(M):
    query = input()
    if query.isdigit():                     
        result.append(revQ[int(query)])
    else:                                   
        result.append(str(Q[query]))
print('\n'.join(result))