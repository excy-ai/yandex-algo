def t(n):
    return n * (n + 1) // 2


def main():
    n = int(input().strip())
    if n == 1:
        print(1)
        return
    dp_u = [0] * (n + 2)
    dp_l = [0] * (n + 2)
    dp_u[1] = 1
    dp_l[1] = 0
    dp_u[2] = 3
    dp_l[2] = 1
    for i in range(3, n + 1):
        dp_u[i] = dp_u[i - 1] + t(i)
        dp_l[i] = dp_l[i - 2] + t(i - 1)
    print(dp_u[n] + dp_l[n] + 1)


if __name__ == '__main__':
    main()
