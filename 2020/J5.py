import sys

sys.setrecursionlimit(10**6)


def DFS(v2c: dict, cell: int, visited: list[bool], M: int, N: int) -> bool:
    if cell == M * N:
        return True
    if cell not in v2c:
        return False
    # visited must be added later
    if visited[cell]:
        return False
    else:
        visited[cell] = True

    for v in v2c[cell]:
        if visited[v]:
            continue
        # consider visited or not
        if DFS(v2c, v, visited, M, N):
            return True

    return False


if __name__ == "__main__":
    M = int(input())
    N = int(input())

    # {key=cell value: value=a list of coordinates}
    v2c = {}
    for m in range(M):
        row = list(map(int, input().split()))
        for n in range(N):
            tmp = (m + 1) * (n + 1)
            if tmp not in v2c:
                v2c[tmp] = [row[n]]
            else:
                v2c[tmp].append(row[n])

    # print(v2c)
    visited = [False] * 1000001
    if DFS(v2c, v2c[1][0], visited, M, N):
        print("yes")
    else:
        print("no")
