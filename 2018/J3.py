if __name__ == "__main__":
    dists = list(map(int, input().split()))

    # print(dists)

    # mat = [[0] * 5] * 5
    mat = [[0] * 5 for _ in range(5)]
    # print(mat)
    for i in range(5):
        for j in range(5):
            if i == j:
                mat[i][j] = 0
            elif i < j:
                d = 0
                for k in range(i, j):
                    d += dists[k]
                mat[i][j] = d
            else:
                mat[i][j] = mat[j][i]

    for i in range(5):
        row = ""
        for j in range(5):
            row += str(mat[i][j]) + " "
        print(row)
