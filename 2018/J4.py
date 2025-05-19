def rotate90anticlockwise(grid: list[list[int]]) -> list[list[int]]:
    N = len(grid)
    res = [[0] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            res[i][j] = grid[j][N - i - 1]

    return res


if __name__ == "__main__":
    N = int(input())
    grid = []

    for _ in range(N):
        grid.append(list(map(int, input().split())))

    corner1 = grid[0][0]
    corner2 = grid[0][N - 1]
    corner3 = grid[N - 1][0]
    corner4 = grid[N - 1][N - 1]

    # 360*I+0
    # 360*I+90
    # 360*I+180
    # 360*I+270

    if corner2 < corner1 and corner2 < corner3 and corner2 < corner4:
        grid = rotate90anticlockwise(grid)
    elif corner3 < corner1 and corner3 < corner2 and corner3 < corner4:
        grid = rotate90anticlockwise(grid)
        grid = rotate90anticlockwise(grid)
        grid = rotate90anticlockwise(grid)
    elif corner4 < corner1 and corner4 < corner2 and corner4 < corner3:
        grid = rotate90anticlockwise(grid)
        grid = rotate90anticlockwise(grid)

    for row in grid:
        s = ""
        for v in row:
            s += str(v) + " "
        print(s)
