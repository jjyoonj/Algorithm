N, M = map(int,input().split())
ns = set()
for i in range(N):
    ns.add(input())

ms = set()
for i in range(M):
    ms.add(input())

all = sorted(list(ns & ms))
        
print(len(all))
for i in all:
    print(i)
