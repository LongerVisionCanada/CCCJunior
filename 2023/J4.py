if __name__ == "__main__":
    C = int(input())

    row1 = []
    row2 = []
    for x in input().split():
        row1.append(int(x))
    for x in input().split():
        row2.append(int(x))

    total = (sum(row1) + sum(row2)) * 3
    for i in range(C - 1):
        if row1[i] == 1 and row1[i + 1] == 1:
            total -= 2
        if row2[i] == 1 and row2[i + 1] == 1:
            total -= 2
        if row1[i] == 1 and row2[i] == 1:
            if i % 2 == 0:
                total -= 2

    if row1[C - 1] == 1 and row2[C - 1] == 1:
        if (C - 1) % 2 == 0:
            total -= 2

    print(total)
