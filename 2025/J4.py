if __name__ == "__main__":
    N = int(input())

    start = input()
    curr = start
    occurs = []
    times = 1

    for i in range(1, N):
        c = input()
        if c == curr:
            times += 1
        else:
            occurs.append(times)
            times = 1
            curr = c

    occurs.append(times)

    lo = len(occurs)
    if lo == 1:
        if start == "P":
            print(1)
        else:
            print(N - 1)
    else:  # 'P' and 'S' alternates
        if start == "P":
            M = max(occurs[1::2]) + 1
            for i in range(2, lo, 2):
                if occurs[i] == 1 and i + 1 < lo:
                    if occurs[i - 1] + 1 + occurs[i + 1] > M:
                        M = occurs[i - 1] + 1 + occurs[i + 1]
            print(M)
        else:
            M = max(occurs[0::2]) + 1
            for i in range(1, lo, 2):
                if occurs[i] == 1 and i + 1 < lo:
                    if occurs[i - 1] + 1 + occurs[i + 1] > M:
                        M = occurs[i - 1] + 1 + occurs[i + 1]
            print(M)
