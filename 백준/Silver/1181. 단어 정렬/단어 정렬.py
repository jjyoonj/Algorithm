N = int(input())
word = []
for i in range(N):
    a = str(input())
    word.append(a)

word = list(set(word))
word.sort()

b = sorted(word, key=lambda x : len(x))

for i in b:
    print(i)