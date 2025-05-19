if __name__ == "__main__":
    N = int(input())
    Xs = [0] * N
    Ys = [0] * N

    for i in range(N):
        X, Y = input().split(",")
        Xs[i] = int(X)
        Ys[i] = int(Y)

    minX = min(Xs)
    maxX = max(Xs)
    minY = min(Ys)
    maxY = max(Ys)

    print(str(minX - 1) + "," + str(minY - 1))
    print(str(maxX + 1) + "," + str(maxY + 1))
