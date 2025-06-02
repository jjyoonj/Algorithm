N,M = map(int, input().split())
A=[]
B=[]

for i in range(N):
    row = list(map(int, input().split()))
    A.append(row)

for j in range(N):
    row = list(map(int, input().split()))
    B.append(row)
for i in range(N):
    temp = [i+j for i,j in zip(A[i],B[i])]
    print(*temp)
   