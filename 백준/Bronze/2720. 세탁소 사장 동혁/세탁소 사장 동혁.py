num = int(input())
Q = 25
D = 10
N = 5
P = 1
money = []
for _ in range(num):
    C = int(input())
    a = C // Q
    C = C % Q
    b = C // D
    C = C % D
    c = C // N
    C = C % N
    d = C // P
    money.extend([a,b,c,d])
for i in range(0, len(money), 4):
    print(*money[i:i+4])