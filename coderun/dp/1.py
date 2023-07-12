n = int(input())
points = sorted(map(int, input().split(' ')))

dp = [0] * n
dp[1] = points[1] - points[0]
if n > 2:
    dp[2] = points[2] - points[0]
    for i in range(3, n):
        dp[i] = min(dp[i - 1], dp[i - 2]) + points[i] - points[i - 1]

print(dp[-1])
