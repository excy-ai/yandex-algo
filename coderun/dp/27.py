from math import floor


def crt(x):
    return floor(x ** (1. / 3))


def solution():
    n = int(input())
    crt_n = crt(n)
    dp = [n + 1] * (n + 1)
    dp[0] = 0
    triples = [x**3 for x in range(1, crt_n + 1)]
    for triple in triples:
        for i in range(n - triple + 1):
            dp[i + triple] = min(dp[i + triple], dp[i] + 1)

    return dp[n]


print(solution())
