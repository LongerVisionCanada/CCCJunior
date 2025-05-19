def isInGrid(grid: list[list[str]], r: int, c: int) -> bool:
    if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]):
        return False

    return True


def DFS(
    W: str,
    grid: list[list[str]],
    r: int,
    c: int,
    dy: int,
    dx: int,
    idx: int,  # next character
    turned: bool,
) -> int:
    if not isInGrid(grid, r + dy, c + dx):
        return 0
    if W[idx] != grid[r + dy][c + dx]:
        return 0
    if idx == len(W) - 1:
        return 1

    if turned:
        return DFS(W, grid, r + dy, c + dx, dy, dx, idx + 1, True)
    else:
        # dot product:
        # a*dy+b*dx=0
        # -dx*dy+dy*dx=0
        # dx*dy+(-dy)*dx=0
        # originally: dy=0,dx=-1=>
        # expecting: dy=+/-1,dx=0
        # originally: dy=1,dx=1=>
        # expecting: dy=1,dx=-1 or dy=-1,dx=1
        return (
            DFS(W, grid, r + dy, c + dx, dy, dx, idx + 1, False)
            + DFS(W, grid, r + dy, c + dx, -dx, dy, idx + 1, True)
            + DFS(W, grid, r + dy, c + dx, dx, -dy, idx + 1, True)
        )


if __name__ == "__main__":
    W = input()
    R = int(input())
    C = int(input())

    # grid = []
    # for _ in range(R):
    #     grid.append(input().split())
    grid = [input().split() for _ in range(R)]

    counter = 0
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if W[0] == grid[r][c]:
                # direction selected
                counter += DFS(W, grid, r, c, -1, -1, 1, False)
                counter += DFS(W, grid, r, c, -1, 0, 1, False)
                counter += DFS(W, grid, r, c, -1, +1, 1, False)
                counter += DFS(W, grid, r, c, 0, +1, 1, False)
                counter += DFS(W, grid, r, c, +1, +1, 1, False)
                counter += DFS(W, grid, r, c, +1, 0, 1, False)
                counter += DFS(W, grid, r, c, +1, -1, 1, False)
                counter += DFS(W, grid, r, c, 0, -1, 1, False)

    print(counter)
