N = int(input())
result = []
for i in range(N):
    a,b = input().split()
    result.append((int(a),b))

result.sort(key=lambda x: x[0])

for i in result:
    print(i[0], i[1])