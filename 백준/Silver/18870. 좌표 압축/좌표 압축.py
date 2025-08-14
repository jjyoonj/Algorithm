N = int(input())
result = list(map(int, input().split()))

sortedlist = sorted(list(set(result)))
dictlist = dict(zip(sortedlist, list(range(len(sortedlist)))))

for x in result:
    print(dictlist[x])