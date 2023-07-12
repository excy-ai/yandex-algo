def main():
    n, k = list(map(int, input().split(' ')))
    dp = [0] * (n + 2)
    dp[1] = 1
    dp[2] = 1
    for i in range(3, n + 1):
        if i > k:
            dp[i] = 2 * dp[i - 1] - dp[i - k - 1]
        elif i <= k:
            dp[i] = 2 * dp[i - 1]
    print(dp[n])


if __name__ == '__main__':
    main()
