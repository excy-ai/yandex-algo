if __name__ == '__main__':
    n = int(input())
    dp = [0] * (n + 3)
    dp[1] = 2
    dp[2] = 4
    dp[3] = 7
    for i in range(4, n + 1):
        dp[i] = dp[i - 3] + dp[i - 2] + dp[i - 1]
    print(dp[n])
