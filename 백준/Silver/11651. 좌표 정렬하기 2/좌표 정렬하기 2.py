N = int(input())

Z = []

for _ in range(N):
    z = list(map(int, input().split()))
    Z.append(z)


Z.sort(key=lambda x: (x[1],x[0]))
for i in Z:
    print(i[0], i[1])
