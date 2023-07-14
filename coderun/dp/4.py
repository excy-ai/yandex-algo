def main():
    n, m = list(map(int, input().split()))
    dp = [[0 for _ in range(m + 2)] for _ in range(n + 2)]
    dp[2][2] = 1
    for i in range(3, n + 2):
        for j in range(3, m + 2):
            dp[i][j] += dp[i - 1][j - 2] + dp[i - 2][j - 1]
    print(dp[n + 1][m + 1])


if __name__ == '__main__':
    main()
