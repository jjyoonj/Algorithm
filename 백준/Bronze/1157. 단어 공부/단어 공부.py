a = input().upper()
wl = list(set(a))

cnt = []
for i in wl:
    count = a.count
    cnt.append(count(i))
    
if cnt.count(max(cnt)) > 1:
    print("?")
else:
    print(wl[(cnt.index(max(cnt)))])