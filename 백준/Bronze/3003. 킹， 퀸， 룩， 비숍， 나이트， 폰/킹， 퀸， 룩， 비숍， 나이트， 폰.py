s = list(map(int, input().split()))
l = [1,1,2,2,2,8]

b=[]
for i in range(len(l)):
    b.append(l[i]-s[i])
#print(b)
for i in b:
    print(i, end=' ')