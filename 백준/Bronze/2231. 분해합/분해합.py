n = int(input())
result = 0

for i in range(1, n+1):
    nums = list(map(int, str(i)))
    result = sum(nums) + i   # 1 + 9 + 8 + 198
    if result == n:
        print(i)
        break
    if i == n:
    	print(0)
     