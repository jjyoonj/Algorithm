N = int(input())
num = list(map(int, input().split()))
avg_list = []
for i in range(N):
    num_max = max(num)
    avg_list.append((num[i]/num_max) * 100)

print(sum(avg_list)/N)