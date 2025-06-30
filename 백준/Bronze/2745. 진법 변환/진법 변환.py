N, B = map(str, input().split())
B = int(B)
N = N[::-1]
dict = {'A':10,'B':11,'C':12,'D':13,'E':14,'F':15,
        'G':16,'H':17,'I':18,'J':19,'K':20,'L':21,
        'M':22,'N':23,'O':24,'P':25,'Q':26,'R':27,
        'S':28,'T':29,'U':30,'V':31,'W':32,'X':33,
        'Y':34,'Z':35}
cc = 0
for i in range(len(N)):
    ch = N[i]
    a = int(ch) if ch.isdigit() else dict[ch]
    b = a * (B**i)
    cc += b
print(cc)