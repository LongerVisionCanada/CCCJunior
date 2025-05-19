def pifunc(n: int, k: int, m: int) -> int:
    if n < k * m:
        return 0
    if n == k * m:
        return 1
    if k == 1 and m <= n:
        return 1

    s = 0
    # m*k<n <=> m <= n//k
    for i in range(m, n // k + 1):
        s += pifunc(n - i, k - 1, i)

    return s


# return piokArr[k][n] = piok(k - 1, n - 1) + piok(k, n-k);

if __name__ == "__main__":
    n = int(input())
    k = int(input())

    print(pifunc(n, k, 1))
