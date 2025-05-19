if __name__ == "__main__":
    X = int(input())
    constraintsX = []

    for i in range(X):
        row = []
        for x in input().split():
            row.append(x)
        constraintsX.append(row)

    Y = int(input())
    constraintsY = []
    for i in range(Y):
        row = []
        for x in input().split():
            row.append(x)
        constraintsY.append(row)

    G = int(input())

    name_2_group = {}
    for i in range(G):
        for x in input().split():
            name_2_group[x] = i

    nbOfViolate = 0
    for cx in constraintsX:
        if name_2_group[cx[0]] != name_2_group[cx[1]]:
            nbOfViolate += 1

    for cy in constraintsY:
        if name_2_group[cy[0]] == name_2_group[cy[1]]:
            nbOfViolate += 1

    print(nbOfViolate)
