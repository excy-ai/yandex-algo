def main():
    n = int(input())
    seq = list(map(int, input().strip().split(' ')))
    dp = [0] * (n + 1)
    dp[0] = 1
    prev = [-1] * (n + 1)
    for idx, v in enumerate(seq):
        if idx == 0:
            continue
        for i in range(idx + 1):
            if v > seq[i] and dp[i] + 1 > dp[idx]:
                dp[idx] = dp[i] + 1
                prev[idx] = i

    idx_it = dp.index(max(dp))
    res = []
    while idx_it != -1:
        res.append(str(seq[idx_it]))
        idx_it = prev[idx_it]
    res.reverse()
    print(' '.join(res))


if __name__ == '__main__':
    main()
