def main():
    n, m = list(map(int, input().split()))
    cost = []
    for i in range(n):
        cost.append(list(map(int, input().split())))
    dp = [[0 for _ in range(m)] for _ in range(n)]
    dp[0][0] = cost[0][0]
    s = 0
    for i in range(n):
        s += cost[i][0]
        dp[i][0] = s
    s = 0
    for j in range(m):
        s += cost[0][j]
        dp[0][j] = s
    for i in range(1, n):
        for j in range(1, m):
            dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + cost[i][j]
    print(dp[-1][-1])


if __name__ == '__main__':
    main()
