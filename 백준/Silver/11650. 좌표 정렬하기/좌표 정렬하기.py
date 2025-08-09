N = int(input())

Z = []

for _ in range(N):
    z = list(map(int, input().split()))
    Z.append(z)
    
Z.sort()
for i in Z:
    print(i[0], i[1])