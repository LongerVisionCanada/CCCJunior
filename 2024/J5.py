import queue


def isOk(patch, row, col) -> bool:
    if row < 0 or row >= len(patch) or col < 0 or col >= len(patch[0]):
        return False

    if patch[row][col] <= 0:
        return False

    return True


def BFS(patch, row, col) -> int:
    scores = patch[row][col]
    q = queue.Queue()
    q.put((row, col))
    patch[row][col] = -1

    while not q.empty():
        r, c = q.get()
        if isOk(patch, r, c - 1):
            scores += patch[r][c - 1]
            patch[r][c - 1] = -1
            q.put((r, c - 1))
        if isOk(patch, r, c + 1):
            scores += patch[r][c + 1]
            patch[r][c + 1] = -1
            q.put((r, c + 1))
        if isOk(patch, r - 1, c):
            scores += patch[r - 1][c]
            patch[r - 1][c] = -1
            q.put((r - 1, c))
        if isOk(patch, r + 1, c):
            scores += patch[r + 1][c]
            patch[r + 1][c] = -1
            q.put((r + 1, c))

    return scores


if __name__ == "__main__":
    R = int(input())
    C = int(input())

    patch = []
    for i in range(R):
        s = input()
        row = []
        for c in s:
            if c == "L":
                row.append(10)
            elif c == "M":
                row.append(5)
            elif c == "S":
                row.append(1)
            else:  # "*"
                row.append(0)
        patch.append(row)

    A = int(input())
    B = int(input())

    print(BFS(patch, A, B))
