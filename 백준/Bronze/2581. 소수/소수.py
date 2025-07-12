M = int(input())
N = int(input())
cnt=[]
for i in range(M, N+1):
    for j in range(2, i+1):
        if i % j == 0:
            if i == j:
                cnt.append(i)
            break
if len(cnt) == 0:
    print(-1)
else:
    print(sum(cnt))
    print(min(cnt))