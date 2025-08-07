result = []
for i in range(5):
    a = int(input())
    result.append(a)
b = sorted(result)

print(sum(result)//5)
print(b[2])