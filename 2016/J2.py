if __name__ == "__main__":
    mat = []
    for _ in range(4):
        row = list(map(int, input().split()))
        mat.append(row)

    s = sum(mat[0])
    magicOrNot = True
    for i in range(1, 4):
        if s != sum(mat[i]):
            magicOrNot = False
            break

    if magicOrNot:
        for i in range(4):
            tmp = 0
            for j in range(4):
                tmp += mat[j][i]
            if s != tmp:
                magicOrNot = False
                break

    if magicOrNot:
        print("magic")
    else:
        print("not magic")
