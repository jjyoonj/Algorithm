N, B = map(int, input().split())
num = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
s = ''
while N!=0:
    s += num[N % B]
    N //= B
    
print(s[::-1])