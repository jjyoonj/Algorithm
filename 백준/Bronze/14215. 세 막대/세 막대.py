x = list(map(int, input().split()))
x.sort()
a,b,c = x
if a + b <= c:
    c = a + b - 1
    print(a+b+c)
else:
    print(a+b+c)