def main():
    n, m = list(map(int, input().split()))
    cost = []
    for i in range(n):
        cost.append(list(map(int, input().split())))
    dp = [[0 for _ in range(m)] for _ in range(n)]
    prev = [[None for _ in range(m)] for _ in range(n)]
    dp[0][0] = cost[0][0]
    s = 0
    for i in range(n):
        s += cost[i][0]
        dp[i][0] = s
        prev[i][0] = 'D'
    s = 0
    for j in range(m):
        s += cost[0][j]
        dp[0][j] = s
        prev[0][j] = 'R'
    prev[0][0] = None
    for i in range(1, n):
        for j in range(1, m):
            if dp[i - 1][j] > dp[i][j - 1]:
                s = dp[i - 1][j]
                prev[i][j] = 'D'
            else:
                s = dp[i][j - 1]
                prev[i][j] = 'R'
            dp[i][j] = s + cost[i][j]
    res = []
    i = -1
    j = -1
    p = prev[i][j]
    while p is not None:
        res += p
        if p == 'D':
            i -= 1
        else:
            j -= 1
        p = prev[i][j]
    res.reverse()
    print(dp[-1][-1])
    print(' '.join(res))


if __name__ == '__main__':
    main()
