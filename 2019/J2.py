if __name__ == "__main__":
    L = int(input())

    res = []
    for l in range(L):
        n, s = input().split()
        N = int(n)
        line = ""
        for _ in range(N):
            line += s
        res.append(line)

    for r in res:
        print(r)
