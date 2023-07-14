from math import inf

n, a, b = map(int, input().split())

dp = [inf] * (n + 1)
dp[0] = 0
dp[1] = 0

for i in range(2, n + 1):
    cur = []
    for j in range(1, i):
        cur += [max(dp[i - j] + a, dp[j] + b)]
    dp[i] = min(cur)

print(dp[-1])
