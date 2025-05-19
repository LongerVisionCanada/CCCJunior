if __name__ == "__main__":
    R = int(input())
    C = int(input())
    M = int(input())

    cost = []

    num = 1
    for i in range(R):
        row = []
        for j in range(C):
            remainder = num % M
            if remainder == 0:
                row.append(M)
            else:
                row.append(remainder)
            num += 1
        cost.append(row)

    for i in range(1, R):
        for j in range(C):
            if j == 0:
                cost[i][j] = min(cost[i - 1][j], cost[i - 1][j + 1]) + cost[i][j]
            elif j == C - 1:
                cost[i][j] = min(cost[i - 1][j - 1], cost[i - 1][j]) + cost[i][j]
            else:
                cost[i][j] = (
                    min(cost[i - 1][j - 1], cost[i - 1][j], cost[i - 1][j + 1])
                    + cost[i][j]
                )

    print(min(cost[R - 1]))
