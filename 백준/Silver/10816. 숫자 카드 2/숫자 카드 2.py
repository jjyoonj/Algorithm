N = int(input())
ns = sorted(list(map(int,input().split())))

M = int(input())
ms = list(map(int, input().split()))

A = {}
for i in ns:
    if i in A:
        A[i] += 1
    else:
        A[i] = 1

result=[]
for i in ms:
    if i in A.keys():
        result.append(A[i])
    else:
        result.append(0)
print(*result)