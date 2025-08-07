n = int(input())

result = []
for i in range(n):
    a = int(input())
    result.append(a)
b = sorted(result)

for i in range(len(b)):
    print(b[i])