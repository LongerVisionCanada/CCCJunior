if __name__ == "__main__":
    N = int(input())
    L = list(map(int, input().split()))

    # [2, 4000]
    # index of hofs is the height of fence
    # index: 0, 1 are ignored
    hofs = [0] * 4001

    # [1,2000]
    # index: 0 is ignored
    hows = [0] * 2001
    # calculate frequency array
    for l in L:
        hows[l] += 1

    # j > i
    for i in range(1, 2001):
        for j in range(i, 2001):
            if i == j:
                hofs[i + j] += hows[i] // 2
            else:
                hofs[i + j] += min(hows[i], hows[j])

    hofs.sort(reverse=True)

    res = str(hofs[0]) + " "

    counter = 1
    for i in range(1, len(hofs)):
        if hofs[i] == hofs[0]:
            counter += 1

    res += str(counter)

    print(res)
