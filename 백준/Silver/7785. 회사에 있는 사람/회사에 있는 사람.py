n = int(input())
S = {}
for i in range(n):
    a,b = input().split()
    S[a] = b

c = [k for k,v in S.items() if v == 'enter']
c.sort(reverse=True)
for i in c:
    print(i)