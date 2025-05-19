if __name__ == "__main__":
    M = int(input())
    N = int(input())
    K = int(input())

    RProcess = [0] * M
    CProcess = [0] * N
    for i in range(K):
        rc, n = input().split()
        if rc == "R":
            RProcess[int(n) - 1] += 1
        else:
            CProcess[int(n) - 1] += 1

    gold = 0
    oddRows = 0
    for m in range(M):
        if RProcess[m] % 2 == 1:
            oddRows += 1
            gold += N

    for n in range(N):
        if CProcess[n] % 2 == 1:
            gold += M
            gold -= 2 * oddRows

    print(gold)
