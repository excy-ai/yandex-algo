def main():
    n = int(input())
    a = []
    b = []
    c = []
    for i in range(n):
        a_, b_, c_ = (list(map(int, input().split())))
        a += [a_]
        b += [b_]
        c += [c_]
    dp = [0] * (n + 1)
    dp[1] = a[0]
    dp[2] = min(b[0], a[1] + a[0])
    for i in range(3, n + 1):
        prev_diff = min(dp[i-1] + a[i - 1], dp[i-2] + b[i-2])
        dp[i] = min(prev_diff, dp[i-3] + c[i-3])
    print(dp[n])


if __name__ == '__main__':
    main()
