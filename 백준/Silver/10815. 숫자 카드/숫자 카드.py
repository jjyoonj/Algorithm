N = int(input())
nlist = set(list(map(int, input().split())))
M = int(input())
mlist = list(map(int, input().split()))

result = []
for i in mlist:
    if i in nlist:
        result.append(1)
    else:
        result.append(0)
        
print(*result)