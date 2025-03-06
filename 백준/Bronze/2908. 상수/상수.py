a,b = input().split()
c=[]
d=[]
for i in str(a):
    c.append(i)
for i in str(b):
    d.append(i)
c.reverse()
d.reverse()
e = int(''.join(map(str, c)))
f = int(''.join(map(str, d)))
if e>f:
    print(e)
else:
    print(f)
