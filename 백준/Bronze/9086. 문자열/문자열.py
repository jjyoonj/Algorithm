a = int(input())
test = []
for i in range(a):
    b = input()
    test.append(b)
for i in range(a):
    print(test[i][0], test[i][-1], sep='')