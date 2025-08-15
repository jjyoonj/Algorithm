N, M = map(int, input().split())
S = []
for i in range(N):
    a = input()
    S.append(a)

check = []  
for i in range(M):
    b = input()
    check.append(b)

cnt = 0
for i in check:
    if i in S:
        cnt += 1

print(cnt)